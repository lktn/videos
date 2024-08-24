from manim import *
config.pixel_height = 1920
config.pixel_width = 1080
class Scene(Scene):
    def construct(self):
        e = ValueTracker(0.01)
        
        plane = PolarPlane(radius_max=3).add_coordinates().shift(UP*5).scale(2)
        graph1 = always_redraw(lambda: ParametricFunction(lambda t: plane.polar_to_point(2*np.cos(6*t), t), t_range = [0, e.get_value()], color=RED))
        dot1 = always_redraw(lambda: Dot(fill_color=WHITE, fill_opacity=0.8).scale(0.5).move_to(graph1.get_end()))
        axes = Axes(x_range = [0, 6.7, 1], x_length=6.5, y_range=[-3, 3, 1], y_length=3).next_to(plane, DOWN, buff=1.5).scale(2)
        axes.add_coordinates()
        graph2 = always_redraw(lambda: axes.plot(lambda x : 2*np.cos(6*x), x_range = [0, e.get_value()], color=RED))
        dot2 = always_redraw(lambda: Dot(fill_color=WHITE, fill_opacity=0.8).scale(0.5).move_to(graph2.get_end()))
        title = MathTex(r"f(\theta)=2\cos(6\theta)", color=WHITE).next_to(axes, DOWN, buff=0.2).scale(2) 
        
        self.play(LaggedStart(Write(plane), Create(axes), Write(title), run_time=3, lag_ratio=0.5))
        self.add(graph1, graph2, dot1, dot2)
        self.play(e.animate.set_value(TAU), run_time=10, rate_func=linear)
        self.wait()
