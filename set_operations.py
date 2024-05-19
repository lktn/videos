from manim import *

config.pixel_height = 1920*2
config.pixel_width = 1080*2
config.frame_height = 16.0
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

class SetOperations(Scene):
    def construct(self):
        set1 = Circle(radius=2, color=PINK).move_to(LEFT)
        a = MathTex(r"A").set_color(PINK).move_to(UP*(-2.5)+RIGHT*(-1.5))
        set1_group = VGroup(set1, a)

        set2 = Circle(radius=2, color=BLUE).move_to(RIGHT)
        b = MathTex(r"B").set_color(BLUE).move_to(UP*(-2.5)+RIGHT*(1.5))
        set2_group = VGroup(set2, b)

        intersection = Intersection(set1, set2, color=PURPLE, fill_opacity=0.5)
        union = Union(set1, set2, color=PURPLE, fill_opacity=0.5)
        diff1 = Difference(set1, set2, color=PURPLE, fill_opacity=0.5)
        diff2 = Difference(set2, set1, color=PURPLE, fill_opacity=0.5)
        exclusion = Exclusion(set1, set2, color=PURPLE, fill_opacity=0.5)

        f1 = MathTex(r"A\cap B").move_to(DOWN*3.5).set_color_by_gradient(PINK, BLUE)
        f2 = MathTex(r"A\cup B").move_to(DOWN*3.5).set_color_by_gradient(PINK, BLUE)
        f3 = MathTex(r"A\setminus B").move_to(DOWN*3.5).set_color_by_gradient(PINK, BLUE)
        f4 = MathTex(r"B\setminus A").move_to(DOWN*3.5).set_color_by_gradient(PINK, BLUE)
        f5 = MathTex(r"A\bigtriangleup B").move_to(DOWN*3.5).set_color_by_gradient(PINK, BLUE)

        self.play(Create(set1_group), Create(set2_group))
        self.play(GrowFromCenter(intersection), Write(f1))
        self.wait(2)
        self.play(ReplacementTransform(intersection, union), TransformMatchingShapes(f1, f2))
        self.wait(2)
        self.play(ReplacementTransform(union, diff1), TransformMatchingShapes(f2, f3))
        self.wait(2)
        self.play(ReplacementTransform(diff1, diff2), TransformMatchingShapes(f3, f4))
        self.wait(2)
        self.play(ReplacementTransform(diff2, exclusion), TransformMatchingShapes(f4, f5))
        self.wait(6)
