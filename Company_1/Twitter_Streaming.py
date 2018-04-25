import sys
import string
import time
from tweepy import Stream
from tweepy.streaming import StreamListener
from Company_1.TwitterMining import get_twitter_client

class Custom_Listener(StreamListener):
    """
    Stream Listener from streaming Twitter Data
    """
    def _init_(self, fname):
        safe_fname = format_filename(fname)
        self.outfile = "stream_output_%s.jsonl" %safe_fname

    def on_data(self, raw_data):

        try:
            with open(self.outfile, 'a') as fi:
                fi.write(raw_data)
                return True
        except BaseException as be:
            sys.stderr.write("Error on_data : {} \n".format(be))
            time.sleep(5)

        return True


    def on_error(self, status_code):
        if status_code == 420:
            sys.stderr.write("Rate Limit Exceeded")
            return False
        else:
            sys.stderr.write("Error {}\n".format(status_code))
            return True


def format_filename(fname):
        """
        Convert file into safe string file
        :return:
        """
        return ''.join(convert_valid(one_char) for one_char in fname)

def convert_valid(one_char):
        """
        Convert a file into '_' if "invalid"
        :return:
        """
        valid_chars = "-_.%s%s" %(string.ascii_letters,string.digits)
        if one_char in valid_chars:
            return one_char
        else:
            return '_'

if __name__== '__main__':
    take_input = "ICO"
    take_input_fname = ' '.join(take_input)
    auth = get_twitter_client()
    twitter_stream = Stream(auth, Custom_Listener(take_input_fname))
    twitter_stream.filter()

