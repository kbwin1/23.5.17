from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!
 
   def test_home(self):
      with app.test_client() as client:
          res= client.get('/')
          html=res.get_data(as_text=True)
          
          self.assertEqual(res.status_code,200)
          self.assertIn('<p>Click on start to play</p>',html)
          self.assertEqual(session['Score'],0)
          self.assertEqual(session['Times_play'],0)


   def test_game(self):
      with app.test_client() as client:
         with client.session_transaction() as change_session:
              change_session['Times_play']=0,
              change_session['Score']=0,
        
         res= client.get('/game')
         html=res.get_data(as_text=True)
             
         self.assertEqual(res.status_code,200)    
         self.assertTrue(session['Board'])
         self.assertTrue('score')
         self.assertTrue('plays')
         self.assertIn('<button>New Board</button>',html)
         
         
   def test_words(self):
      with app.test_client() as client:
          with client.session_transaction() as change_session:
              change_session['Board']=[['O', 'I', 'Y', 'V', 'J'],
                                       ['K', 'G', 'X', 'Q', 'G'],
                                       ['I', 'N', 'O', 'S', 'E'],
                                       ['L', 'M', 'A', 'K', 'V'],
                                       ['Q', 'U', 'A', 'B', 'Q']]
          res= client.get('/check?word=no')
          self.assertEqual(res.json['result'], 'ok')
          res= client.get('/check?word=monkey')
          self.assertEqual(res.json['result'], 'not-on-board')
          res= client.get('/check?word=jkafhjka')
          self.assertEqual(res.json['result'], 'not-word')       
          
          
   def test_endGame(self):
      with app.test_client() as client:
         with client.session_transaction() as change_session:
              change_session['Times_play']=1
              change_session['Score']= 4
              
         res= client.get('/score')
         
         self.assertEqual(session['Score'],4)
         self.assertEqual(session['Times_play'],1)
         self.assertTrue('max_score')
