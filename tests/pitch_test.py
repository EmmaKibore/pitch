import unittest
from models import pitch
pitch = pitch.Pitch

class PitchTest(unittest.TestCase):
    '''
    Test Class to test teh Behaviourof the Pitch class
    '''
    def Setup(self):
        '''
        set up method that will run before every Test
        '''

        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_pitch = Pitch(id=50,title = 'My pitch',content='I can pitch all day long',category ='But wont',user_id = 10)

def tearDown(self):
        Review.query.delete()
        User.query.delete()
def test_check_instance_variables(self):
        self.assertEquals(self.new_review.movie_id,12345)
        self.assertEquals(self.new_review.movie_title,'Review for movies')
        self.assertEquals(self.new_review.image_path,"https://image.tmdb.org/t/p/w500/jdjdjdjn")
        self.assertEquals(self.new_review.movie_review,'This movie is the best thing since sliced bread')
        self.assertEquals(self.new_review.user,self.user_James)


    def test_save_review(self):
        self.new_review.save_review()
        self.assertTrue(len(Review.query.all())>0)


def test_get_review_by_id(self):

        self.new_review.save_review()
        got_reviews = Review.get_reviews(12345)
        self.assertTrue(len(got_reviews) == 1)
    
