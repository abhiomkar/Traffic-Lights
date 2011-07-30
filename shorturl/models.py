from django.db import models
import random

# TODO
# 
#

# Should not accept the long url of self - domain e.g., abhiomkar.in & abhio.me
# Should accept only valid URLs

# How did I generate the random set of ALPHABET?
# >>> ALPHABET = ''.join(set(map(chr, range(ord('a'), ord('z') + 1)) + map(chr, range(ord('A'), ord('Z') + 1)) + map(str, range(0, 10))) - set("IlO0"))
# >>> shuffle(ALPHABET)
# PS: IlO0 are removed from ALPHABET for the confusion in the Short URL code read
ALPHABET = "pX9znxm2wWHd5vtKFMDsr6fTcZGkUeJ4iLP8YECBRujaSNq3ohA1VQ7bgy"

def _shuffle(length):
    """ Return Shuffle of a-z, A-Z and 0-9 and get first 3 literals 
    """
    return ''.join(random.sample(map(chr, range(ord('a'), ord('z') + 1)) + map(chr, range(ord('A'), ord('Z') + 1)) + map(str, range(0, 10)), length))

class Setting(models.Model):
    shorturl_code_length = models.IntegerField(max_length=5)
    last_number = models.IntegerField(max_length=10)

class URL(models.Model):
    long_url = models.CharField(max_length=9999)
    shorturl_code = models.CharField(max_length=25, primary_key=True)
    username = models.CharField(max_length=50, default="guest")
    date_created = models.DateTimeField(auto_now_add=True)
    click_count = models.IntegerField(max_length=10, default='0')

    class Meta:
        unique_together = ("shorturl_code", "username")

    def _getLastNumber(self):
        """ returns the last number
            Return Type: Integer
        """
        # TODO:
        # - Handle the Table Doesn't Exist Failure
        # - Handle the Table with No Rows Error
        return Setting.objects.all()[0].last_number
    
    def _increaseLastNumber(self):
        """ Increases the last number
            Returns Almost nothing
        """

        _setting = Setting.objects.all()[0]
        _setting.last_number += 1
        _setting.save()
        return True

    def _base_encode(self, num, alphabet=ALPHABET):
        """ Encode a number in Base X

            `num`: The number to encode
            `alphabet`: The alphabet to use for encoding
        """
        
        if (num == 0):
            return alphabet[0]
        arr = []
        base = len(alphabet)
        while num:
            rem = num % base
            num = num // base
            arr.append(alphabet[rem])
        arr.reverse()
        return ''.join(arr)

    def _generateUniqueCode(self):
        """ Generates Unique Short URL Code
            Return Type: String
        """

        while True:
            _last_number = self._getLastNumber()
            _random_short_code = self._base_encode(_last_number)

            _short_code_exists = URL.objects.filter(shorturl_code=_random_short_code)
            if _short_code_exists:
                self._increaseLastNumber()
            else:
                break
        
        return _random_short_code

    def getLongURL(self, code):
        _url = URL.objects.filter(shorturl_code=code)
        if _url:
            return _url[0].long_url
        else:
            return ''

    def saveURL(self, url, user="guest"):
        """ Generate Short URL and Save it
        """
        # Check if the (url, user) already exists in the database
        # Return the short URL if exists otherwise, generate new short URL
        
        _url_exists = URL.objects.filter(long_url=url, username=user)

        if _url_exists:
            return _url_exists[0].shorturl_code
        else:
            pass

        # Generate Short URL Code
        _random_short_code = self._generateUniqueCode()

        _url = URL(long_url = url, 
                   shorturl_code = _random_short_code, 
                   username = user)
        _url.save()

        return _url.shorturl_code

