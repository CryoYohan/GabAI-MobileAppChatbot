from kivy.app import App
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.uix.widget import  Widget
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x,velocity_y)
    # Latest Position = Current Velocity + Current Position
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


# Update - moving the ball by calling the move() and other stuff
class PongGame(Widget):
    ball = ObjectProperty(None)

    def serve_ball(self):
        self.ball.velocity = Vector(4,0).rotate(randint(0,360))

    def update(self,dt):
        self.ball.move()

        # bounce off top and bottom
        if (self.ball.y < 20) or (self.ball.y > self.height-20):
            self.ball.velocity_y *= -1
        # bounce off left and right
        if (self.ball.x < 20) or (self.ball.x > self.width-20):
            self.ball.velocity_x *= -1


class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update,1.0/60.0)
        return game

PongApp().run()