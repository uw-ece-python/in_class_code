import pytest
from pets import *

class TestDog:

    def test_dog_happy_path(self):
        my_dog = Dog("blue")

        assert my_dog.color == "blue"

    def test_dog_jump(self):
        ## Setup
        my_dog = Dog("gray")
        assert my_dog.jump_count == 0

        my_dog.jump()

        assert my_dog.jump_count == 1


    def test_husky_jump_once(self):
        ## Setup
        my_dog = Husky()
        assert my_dog.jump_count == 0

        my_dog.jump()

        assert my_dog.jump_count == 10

class TestHusky:
    def test_husky_jump_second(self):
        ## Setup
        my_dog = Husky()
        assert my_dog.jump_count == 0

        my_dog.jump()

        assert my_dog.jump_count == 10
