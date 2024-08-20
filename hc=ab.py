from manim import *
import math

config.pixel_height = 2880
config.pixel_width = 1620

class PythagorasHeight(Scene):
	def construct(self):
		self.wait(1)
		self.build_triangle()
		self.add_side_lengths()
		self.build_tilted_rect()
		self.slice_and_rearrange_rect()
		self.show_rect_height_and_hypotenuse()
		self.separate_triangle_and_rect()
		self.respawn_tilted_rect()
		self.equate_rects()
		self.write_rect_area()
		self.write_tilted_rect_area()
		self.do_math()

	def build_triangle(self):
		points = [
			[ 2,  1.5, 0],
			[ 2, -1.5, 0],
			[-2, -1.5, 0]
		]

		self.colors = [RED, BLUE, TEAL, YELLOW]
		self.triangle = VGroup(*[Line(points[i], points[(i + 1) % 3], color=self.colors[i]) for i in range(3)])

		ra = RightAngle(Line(points[1], points[0]), Line(points[1], points[2]), length=0.4, stroke_width=2)

		self.triangle += ra
		self.play(Create(VGroup(self.triangle, ra).rotate(math.atan2(4,3) + PI / 2)))

		p_point = self.triangle[2].get_projection(self.triangle[1].get_start())
		p_line = DashedLine(self.triangle[1].get_start(), p_point, color=self.colors[3])
		p_ra = RightAngle(p_line, self.triangle[2], quadrant=[-1,-1], length=0.3, stroke_width=2)
		p = VGroup(p_line, p_ra)

		self.play(Create(p_line, run_time=0.4), Create(p_ra, run_time=0.4))
		self.triangle += p
		self.wait(0.2)

	def add_side_lengths(self):
		self.height = MathTex("h", color=self.colors[3]).move_to(self.triangle[4].get_center()+RIGHT*0.2).scale(1.1)
		self.side_lengths = VGroup(
			MathTex("a", color=self.colors[0]).move_to(self.triangle[0].get_center()+UP*0.3+LEFT*0.3).scale(1.1),
			MathTex("b", color=self.colors[1]).move_to(self.triangle[1].get_center()+UP*0.3+RIGHT*0.3).scale(1.1),
			self.height
		)

		self.triangle += self.side_lengths
		self.play(Write(self.side_lengths))
		self.wait(1)

	def build_tilted_rect(self):
		rect_points = [
			self.triangle[0].get_start(),
			self.triangle[1].get_start(),
			self.triangle[2].get_start(),
			self.triangle[1].get_start() * -1
		]

		self.tilted_rect_lines = VGroup(
			Line(rect_points[0], rect_points[1], color=self.colors[0]),
			Line(rect_points[1], rect_points[1], color=self.colors[1]),
			Line(rect_points[1], rect_points[0], color=self.colors[0]),
			Line(rect_points[0], rect_points[0], color=self.colors[1])
		)
		target_tilted_rect_lines = VGroup(
			Line(rect_points[0], rect_points[1], color=self.colors[0]),
			Line(rect_points[1], rect_points[2], color=self.colors[1]),
			Line(rect_points[2], rect_points[3], color=self.colors[0]),
			Line(rect_points[3], rect_points[0], color=self.colors[1])
		)

		self.tilted_rect = VGroup(Rectangle(width=0, height=3, fill_opacity=0.2, color=PURPLE).rotate(math.atan2(4,3)+PI/2).move_to(self.triangle[0]))
		target_tilted_rect = Rectangle(width=4, height=3, fill_opacity=0.2, color=PURPLE).rotate(math.atan2(4,3)+PI/2).move_to(self.triangle[2])

		self.play(
			FadeIn(self.tilted_rect),
			FadeIn(self.tilted_rect_lines)
		)
		self.play(
			Transform(self.tilted_rect[0], target_tilted_rect),
			*[
				Transform(self.tilted_rect_lines[i], target_tilted_rect_lines[i])
				for i in range(4)
			]
		)
		self.tilted_rect[0] = target_tilted_rect
		self.tilted_rect += self.tilted_rect_lines
		self.wait(1)

	def slice_and_rearrange_rect(self):
		points = {
			"A": self.triangle[0].get_start(),
			"B": self.triangle[1].get_start(),
			"C": self.triangle[2].get_start(),
			"D": self.triangle[1].get_start() * -1,
			"hB": self.triangle[2].get_projection(self.triangle[1].get_start()),
			"hD": self.triangle[2].get_projection(self.triangle[1].get_start()*-1),
			"AxBy": [self.triangle[0].get_start()[0], self.triangle[1].get_start()[1], 0],
			"CxBy": [self.triangle[2].get_start()[0], self.triangle[1].get_start()[1], 0]
		}

		tris = [[points[a] for a in ["A", "B",  "C"]],
				[points[a] for a in ["A", "D", "hD"]],
				[points[a] for a in ["C", "D", "hD"]]]

		tri_polys = VGroup(*map(lambda a: VGroup(Polygon(*a, fill_opacity=0.2, stroke_opacity=0, color=PURPLE)), tris))
		tri_polys[0].add(
			Line(tris[0][0], tris[0][1], color=self.colors[0]),
			Line(tris[0][1], tris[0][2], color=self.colors[1]),
			Line(tris[0][2], tris[0][0], color=self.colors[2])
		)
		tri_polys[1].add(
			Line(tris[1][0], tris[1][1], color=self.colors[1]),
			Line(tris[1][1], tris[1][2], color=self.colors[3]),
			Line(tris[1][2], tris[1][0], color=self.colors[2], stroke_opacity=0)
		)
		tri_polys[2].add(
			Line(tris[2][0], tris[2][1], color=self.colors[0]),
			Line(tris[2][1], tris[2][2], color=self.colors[3]),
			Line(tris[2][2], tris[2][0], color=self.colors[2], stroke_opacity=0)
		)
		
		sect_lines = VGroup(Line(points["D"], points["hD"], color=self.colors[3]))

		self.play(
			*map(Create, sect_lines)
		)
		self.tilted_rect -= self.tilted_rect_lines
		self.remove(self.tilted_rect, self.tilted_rect_lines, *sect_lines)
		self.add(*tri_polys)
		self.play(
			tri_polys[1].animate.shift(LEFT+DOWN),
			tri_polys[2].animate.shift(RIGHT+DOWN)
		)
		self.play(tri_polys[1].animate.move_to(self.triangle[1].get_center()))
		self.play(tri_polys[2].animate.move_to(self.triangle[0].get_center()))

		sect_lines = VGroup(
			Line(points["B"], points["C"], color=self.colors[1]),
			Line(points["A"], points["B"], color=self.colors[0])
		)

		self.rect = VGroup(Rectangle(width=5, height=12/5, fill_opacity=0.2, color=GREEN).set_y(1.2))
		self.rect.add(VGroup(
			Line(points["A"], points["AxBy"], color=self.colors[3]),
			Line(points["C"], points["CxBy"], color=self.colors[3]),
			Line(points["A"], points["C"], color=self.colors[2]),
			Line(points["CxBy"], points["AxBy"], color=self.colors[2])
		))

		self.play(
			tri_polys[1][3].animate.set_opacity(1),
			tri_polys[2][3].animate.set_opacity(1),
			*map(lambda a: a[0].animate.set_color(GREEN), tri_polys)
		)
		self.remove(*tri_polys)
		self.add(self.rect)
		self.play(FadeOut(sect_lines, run_time=0.4))

		self.wait(0.2)

	def show_rect_height_and_hypotenuse(self):
		self.hypotenuse = MathTex("c", color=self.colors[2]).move_to(self.triangle[2].get_center()+DOWN*0.5).scale(1.1)
		self.play(Write(self.hypotenuse))
		self.triangle += self.hypotenuse

		self.rect_height = self.height.copy()
		perpendicular_line_copy = self.triangle[4][0].copy()
		self.play(
			self.rect_height.animate.move_to(self.rect[0].get_left()+LEFT*0.3),
			perpendicular_line_copy.animate.move_to(self.rect[0].get_left()).set_opacity(0)
		)

		self.rect += self.hypotenuse.copy()
		self.rect += self.rect_height
		self.remove(perpendicular_line_copy)
		self.wait(0.8)

	def separate_triangle_and_rect(self):
		self.play(
			self.triangle.animate.shift(DOWN*3),
			self.rect.animate.shift(UP)
		)

		self.remove(self.rect)
		self.add(self.rect)
		self.wait(1)

	def respawn_tilted_rect(self):
		self.tilted_rect += self.tilted_rect_lines
		self.tilted_rect.move_to(self.triangle[2])
		self.tilted_rect += (self.side_lengths - self.height).copy()
		self.play(FadeIn(self.tilted_rect))
		self.wait(1)

	def equate_rects(self):
		self.equal_sign = SingleStringMathTex("=")
		self.rects_are_equal = VGroup(self.rect, self.equal_sign, self.tilted_rect)
		pos = self.rect.get_center()
		self.play(
			FadeIn(self.equal_sign),
			self.rects_are_equal.animate.arrange(buff=0.3).set_y(pos[1]+1)
		)
		self.wait(1)

	def _colorize_tex(self, object):
		if a := object.get_part_by_tex("a"):
			a.set_color(self.colors[0])
		if a := object.get_part_by_tex("b"):
			a.set_color(self.colors[1])
		if a := object.get_part_by_tex("c"):
			a.set_color(self.colors[2])
		if a := object.get_part_by_tex("h"):
			a.set_color(self.colors[3])

	def write_rect_area(self):
		self.rect_area = MathTex("h","c").move_to(self.rect[0]).scale(1.1)
		self._colorize_tex(self.rect_area)
		self.play(
			ReplacementTransform(self.rect[3], self.rect_area[0]),
			ReplacementTransform(self.rect[2], self.rect_area[1])
		)
		self.remove(*self.rect_area[:2])
		self.add(self.rect_area)

	def write_tilted_rect_area(self):
		self.tilted_rect_area = MathTex("a","b").move_to(self.tilted_rect[0]).scale(1.1)
		self._colorize_tex(self.tilted_rect_area)

		self.play(
 			ReplacementTransform(self.tilted_rect[2][0], self.tilted_rect_area[0]),
			ReplacementTransform(self.tilted_rect[2][1], self.tilted_rect_area[1])
		)
		self.remove(self.tilted_rect_area[:2])
		self.add(self.tilted_rect_area)

	def do_math(self):
		self.rects_are_equal -= self.equal_sign

		pos = self.rects_are_equal.get_center()

		initial_formula = MathTex("h","c","=","a","b").move_to(pos).scale(1.1)
		self._colorize_tex(initial_formula)

		orig_poses = [a.get_center() for a in initial_formula]

		initial_formula[4].move_to(self.tilted_rect_area[1])
		initial_formula[3].move_to(self.tilted_rect_area[0])
		initial_formula[2].move_to(self.equal_sign[0])
		initial_formula[1].move_to(self.rect_area[1])
		initial_formula[0].move_to(self.rect_area[0])

		self.remove(self.rect_area, self.tilted_rect_area, self.equal_sign)
		self.add(initial_formula)

		self.wait(0.75)

		self.play(
			FadeOut(self.rects_are_equal, run_time=0.4),
			*[
				initial_formula[i].animate(run_time=1.2).move_to(orig_poses[i]) for i in range(5)
			]
		)
		self.remove(self.tilted_rect, self.rect)
		self.wait(1)
		self.play(Circumscribe(initial_formula))
		self.wait(1)