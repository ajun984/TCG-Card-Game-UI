import math

from battle_field.components.opponent_deck import OpponentDeck
from battle_field.components.opponent_hand_panel import OpponentHandPanel
from battle_field.components.opponent_lost_zone import OpponentLostZone
from battle_field.components.opponent_main_character import OpponentMainCharacter
from battle_field.components.opponent_tomb import OpponentTomb
from battle_field.components.opponent_trap import OpponentTrap
from battle_field.components.opponent_unit_field import OpponentUnitField
from battle_field.components.your_lost_zone import YourLostZone
from battle_field.components.your_tomb import YourTomb
from battle_field.components.your_trap import YourTrap
from image_shape.oval_image import OvalImage
from image_shape.rectangle_image import RectangleImage
from opengl_shape.oval import Oval
from opengl_shape.shape import Shape
from OpenGL import GL

import tkinter
import unittest

from OpenGL.GL import *
from OpenGL.GLU import *
from pyopengltk import OpenGLFrame

from pre_drawed_image_manager.pre_drawed_image import PreDrawedImage
from opengl_shape.rectangle import Rectangle


class YourCardDeck:
    __pre_drawed_image_instance = PreDrawedImage.getInstance()

    def __init__(self, local_translation=(0, 0), scale=1):
        self.pre_drawed_opponent_card_deck = None
        self.shapes = []
        self.local_translation = local_translation
        self.scale = scale

    def get_your_card_deck_shapes(self):
        return self.shapes

    def change_local_translation(self, _translation):
        self.local_translation = _translation

    def add_shape(self, shape):
        shape.local_translate(self.local_translation)
        self.shapes.append(shape)

    def create_your_card_deck(self, image_data, vertices):
        your_card_deck = RectangleImage(image_data=image_data,
                                        vertices=vertices)
        self.add_shape(your_card_deck)

    def init_shapes(self):
        self.__pre_drawed_image_instance.pre_draw_your_card_deck()

        self.create_your_card_deck(
            image_data=self.__pre_drawed_image_instance.get_pre_draw_your_card_deck(),
            vertices=[(1700, 590), (1850, 590), (1850, 790), (1700, 790)])
        self.create_your_card_deck(
            image_data=self.__pre_drawed_image_instance.get_pre_draw_your_card_deck(),
            vertices=[(1705, 595), (1855, 595), (1855, 795), (1705, 795)])
        self.create_your_card_deck(
            image_data=self.__pre_drawed_image_instance.get_pre_draw_your_card_deck(),
            vertices=[(1710, 600), (1860, 600), (1860, 800), (1710, 800)])
        self.create_your_card_deck(
            image_data=self.__pre_drawed_image_instance.get_pre_draw_your_card_deck(),
            vertices=[(1715, 605), (1865, 605), (1865, 805), (1715, 805)])
        self.create_your_card_deck(
            image_data=self.__pre_drawed_image_instance.get_pre_draw_your_card_deck(),
            vertices=[(1720, 610), (1870, 610), (1870, 810), (1720, 810)])


class YourMainCharacter:
    __pre_drawed_image_instance = PreDrawedImage.getInstance()

    def __init__(self, local_translation=(0, 0), scale=1):
        self.pre_drawed_main_character = None
        self.shapes = []
        self.local_translation = local_translation
        self.scale = scale

    def change_main_character_translation(self, _translation):
        self.local_translation = _translation

    def get_main_character_shapes(self):
        return self.shapes

    def add_shape(self, shape):
        shape.local_translate(self.local_translation)
        self.shapes.append(shape)

    def create_main_character(self, image_data, center, radius_x, radius_y):
        main_character_illustration = OvalImage(image_data=image_data,
                                                center=center,
                                                radius_x=radius_x,
                                                radius_y=radius_y)
        print(f"main_character_illustration{main_character_illustration}")
        print(type(main_character_illustration))
        self.add_shape(main_character_illustration)

    def init_your_main_character_shapes(self):
        radius_y = 40
        radius_x = radius_y * ((1 + math.sqrt(5)) / 2)
        self.__pre_drawed_image_instance.pre_draw_your_main_character()

        self.create_main_character(image_data=self.__pre_drawed_image_instance.get_pre_draw_your_main_character(),
                                   center=(960, 1034),
                                   radius_x=radius_x,
                                   radius_y=radius_y)


class YourHandPanel:
    __pre_drawed_image_instance = PreDrawedImage.getInstance()

    def __init__(self, local_translation=(0, 0), scale=1):
        self.pre_drawed_your_hand = None
        self.shapes = []
        self.local_translation = local_translation
        self.scale = scale

        self.pickable_card_list = []

    def change_local_translation(self, _translation):
        self.local_translation = _translation

    def get_your_hand_panel_shapes(self):
        return self.shapes

    def get_pickable_card_list(self):
        return self.pickable_card_list

    def add_shape(self, shape):
        shape.local_translate(self.local_translation)
        self.shapes.append(shape)

    def create_hand_panel(self, image_data, vertices):
        hand_panel = RectangleImage(image_data=image_data,
                                    vertices=vertices)
        self.add_shape(hand_panel)

    def init_shapes(self):
        self.__pre_drawed_image_instance.pre_draw_your_hand_panel()

        self.create_hand_panel(image_data=self.__pre_drawed_image_instance.get_pre_draw_your_hand_panel(),
                               vertices=[(300, 830), (1600, 830), (1600, 980), (300, 980)])


class YourUnitField:
    __pre_drawed_image_instance = PreDrawedImage.getInstance()

    def __init__(self, local_translation=(0, 0), scale=1):
        self.pre_drawed_your_hand = None
        self.shapes = []
        self.local_translation = local_translation
        self.scale = scale

        self.pickable_card_list = []

    def change_local_translation(self, _translation):
        self.local_translation = _translation

    def get_your_unit_field_shapes(self):
        return self.shapes

    def get_pickable_card_list(self):
        return self.pickable_card_list

    def add_shape(self, shape):
        shape.local_translate(self.local_translation)
        self.shapes.append(shape)

    def create_unit_field(self, image_data, vertices):
        unit_field = RectangleImage(image_data=image_data,
                                    vertices=vertices)
        self.add_shape(unit_field)

    def init_shapes(self):
        self.__pre_drawed_image_instance.pre_draw_your_unit_field()
        # (300, 800), (1600, 800), (1600, 950), (300, 950)
        self.create_unit_field(image_data=self.__pre_drawed_image_instance.get_pre_draw_your_unit_field(),
                               vertices=[(300, 580), (1600, 580), (1600, 730), (300, 730)])


class BattleFieldEnvironment:
    __pre_drawed_image_instance = PreDrawedImage.getInstance()

    def __init__(self, local_translation=(0, 0), scale=1):
        self.shapes = []
        self.local_translation = local_translation
        self.scale = scale

    def get_environment_shapes(self):
        return self.shapes

    def change_local_translation(self, _translation):
        self.local_translation = _translation

    def add_shape(self, shape):
        shape.local_translate(self.local_translation)
        self.shapes.append(shape)

    def create_environment(self, image_data, vertices):
        environment_illustration = RectangleImage(image_data=image_data,
                                                  vertices=vertices)
        self.add_shape(environment_illustration)

    def init_shapes(self):
        self.__pre_drawed_image_instance.pre_draw_battle_field_environment()

        self.create_environment(image_data=self.__pre_drawed_image_instance.get_pre_draw_battle_field_environment(),
                                vertices=[(400, 490), (500, 490), (500, 590), (400, 590)])


class PreDrawedBattleFieldFrameRefactor(OpenGLFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        self.width = screen_width
        self.height = screen_height

        self.opponent_tomb = OpponentTomb()
        self.opponent_tomb.init_shapes()
        self.opponent_tomb_shapes = self.opponent_tomb.get_tomb_shapes()

        self.opponent_lost_zone = OpponentLostZone()
        self.opponent_lost_zone.init_shapes()
        self.opponent_lost_zone_shapes = self.opponent_lost_zone.get_lost_zone_shapes()

        self.opponent_trap = OpponentTrap()
        self.opponent_trap.init_shapes()
        self.opponent_trap_shapes = self.opponent_trap.get_trap_shapes()

        self.opponent_card_deck = OpponentDeck()
        self.opponent_card_deck.init_shapes()
        self.opponent_card_deck_shapes = self.opponent_card_deck.get_opponent_card_deck_shapes()

        self.opponent_main_character = OpponentMainCharacter()
        self.opponent_main_character.init_opponent_main_character_shapes()
        self.opponent_main_character_shapes = self.opponent_main_character.get_main_character_shapes()

        self.opponent_hand_panel = OpponentHandPanel()
        self.opponent_hand_panel.init_shapes()
        self.opponent_hand_panel_shapes = self.opponent_hand_panel.get_opponent_hand_panel_shapes()

        self.opponent_unit_field = OpponentUnitField()
        self.opponent_unit_field.init_shapes()
        self.opponent_unit_field_shapes = self.opponent_unit_field.get_opponent_unit_field_shapes()

        self.your_tomb = YourTomb()
        self.your_tomb.init_shapes()
        self.your_tomb_shapes = self.your_tomb.get_tomb_shapes()

        self.your_lost_zone = YourLostZone()
        self.your_lost_zone.init_shapes()
        self.your_lost_zone_shapes = self.your_lost_zone.get_lost_zone_shapes()

        self.your_trap = YourTrap()
        self.your_trap.init_shapes()
        self.your_trap_shapes = self.your_trap.get_trap_shapes()

        self.your_card_deck = YourCardDeck()
        self.your_card_deck.init_shapes()
        self.your_card_deck_shapes = self.your_card_deck.get_your_card_deck_shapes()

        self.your_main_character = YourMainCharacter()
        self.your_main_character.init_your_main_character_shapes()
        self.your_main_character_shapes = self.your_main_character.get_main_character_shapes()

        self.your_hand_panel = YourHandPanel()
        self.your_hand_panel.init_shapes()
        self.your_hand_panel_shapes = self.your_hand_panel.get_your_hand_panel_shapes()

        self.your_unit_field = YourUnitField()
        self.your_unit_field.init_shapes()
        self.your_unit_field_shapes = self.your_unit_field.get_your_unit_field_shapes()

        self.battle_field_environment = BattleFieldEnvironment()
        self.battle_field_environment.init_shapes()
        self.battle_field_environment_shapes = self.battle_field_environment.get_environment_shapes()

        self.bind("<Configure>", self.on_resize)

    def initgl(self):
        glClearColor(1.0, 1.0, 1.0, 0.0)
        glOrtho(0, self.width, self.height, 0, -1, 1)

        self.tkMakeCurrent()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for opponent_tomb_shape in self.opponent_tomb_shapes:
            opponent_tomb_shape.draw()

        for opponent_lost_zone_shape in self.opponent_lost_zone_shapes:
            opponent_lost_zone_shape.draw()

        for opponent_trap_shape in self.opponent_trap_shapes:
            opponent_trap_shape.draw()

        for opponent_card_deck_shape in self.opponent_card_deck_shapes:
            opponent_card_deck_shape.draw()

        for opponent_main_character_shape in self.opponent_main_character_shapes:
            opponent_main_character_shape.draw()

        for opponent_hand_panel_shape in self.opponent_hand_panel_shapes:
            opponent_hand_panel_shape.draw()

        for opponent_unit_field_shape in self.opponent_unit_field_shapes:
            opponent_unit_field_shape.draw()

        for your_tomb_shape in self.your_tomb_shapes:
            your_tomb_shape.draw()

        for your_lost_zone_shape in self.your_lost_zone_shapes:
            your_lost_zone_shape.draw()

        for your_trap_shape in self.your_trap_shapes:
            your_trap_shape.draw()

        for your_card_deck_shape in self.your_card_deck_shapes:
            your_card_deck_shape.draw()

        for your_main_character_shape in self.your_main_character_shapes:
            your_main_character_shape.draw()

        for your_hand_panel_shape in self.your_hand_panel_shapes:
            your_hand_panel_shape.draw()

        for your_unit_field_shape in self.your_unit_field_shapes:
            your_unit_field_shape.draw()

        for battle_field_environment_shape in self.battle_field_environment_shapes:
            battle_field_environment_shape.draw()

        self.tkSwapBuffers()

    def reshape(self, width, height):
        print(f"Reshaping window to width={width}, height={height}")
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0, width, height, 0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def on_resize(self, event):
        print("Handling resize event")
        self.reshape(event.width, event.height)

    def redraw(self):
        self.tkMakeCurrent()
        # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        #
        # for opponent_tomb_shape in self.opponent_tomb_shapes:
        #     opponent_tomb_shape.draw()
        #
        # for opponent_lost_zone_shape in self.opponent_lost_zone_shapes:
        #     opponent_lost_zone_shape.draw()
        #
        # for opponent_trap_shape in self.opponent_trap_shapes:
        #     opponent_trap_shape.draw()
        #
        # for opponent_card_deck_shape in self.opponent_card_deck_shapes:
        #     opponent_card_deck_shape.draw()
        #
        # for opponent_main_character_shape in self.opponent_main_character_shapes:
        #     opponent_main_character_shape.draw()
        #
        # for opponent_hand_panel_shape in self.opponent_hand_panel_shapes:
        #     opponent_hand_panel_shape.draw()
        #
        # for opponent_unit_field_shape in self.opponent_unit_field_shapes:
        #     opponent_unit_field_shape.draw()
        #
        # for your_tomb_shape in self.your_tomb_shapes:
        #     your_tomb_shape.draw()
        #
        # for your_lost_zone_shape in self.your_lost_zone_shapes:
        #     your_lost_zone_shape.draw()
        #
        # for your_trap_shape in self.your_trap_shapes:
        #     your_trap_shape.draw()
        #
        # for your_card_deck_shape in self.your_card_deck_shapes:
        #     your_card_deck_shape.draw()
        #
        # for your_main_character_shape in self.your_main_character_shapes:
        #     your_main_character_shape.draw()
        #
        # for your_hand_panel_shape in self.your_hand_panel_shapes:
        #     your_hand_panel_shape.draw()
        #
        # for your_unit_field_shape in self.your_unit_field_shapes:
        #     your_unit_field_shape.draw()
        #
        # for battle_field_environment_shape in self.battle_field_environment_shapes:
        #     battle_field_environment_shape.draw()

        self.tkSwapBuffers()



class TestDrawBattleFieldRefactor(unittest.TestCase):

    def test_draw_battle_field_refactor(self):
        root = tkinter.Tk()
        root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}-0-0")
        root.deiconify()

        pre_drawed_battle_field_frame = PreDrawedBattleFieldFrameRefactor(root)
        pre_drawed_battle_field_frame.pack(fill=tkinter.BOTH, expand=1)
        root.update_idletasks()

        def animate():
            pre_drawed_battle_field_frame.redraw()
            # root.after(17, animate)
            root.after(33, animate)

        root.after(0, animate)

        root.mainloop()


if __name__ == '__main__':
    unittest.main()
