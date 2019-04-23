import unittest
from app.models import pitch

class PitchTest(unittest.TestCase):
    '''
    Test Class to test teh Behaviourof the Pitch class
    '''
    def Setup(self):
        '''
        set up method that will run before every Test
        '''

        self.new_pitch = Pitch(id=50,title = 'My pitch',content='I can pitch all day long',category ='But wont',user_id = 10)
