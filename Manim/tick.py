from manim import *
s_300 = "#73EA69"
s_100 = "#B9F5B4"
s_50 = "#DCFAD9"
# manim -pql --gif beautiful_3d_circle.py Beautiful3DCircle
# manim -r 2560,1440 --fps 120 tick.py FilledCircle 
# manim -r 2560,1440 --fps 120 tick.py FilledCircle --format=webm --transparent


class GreenCircleTick(Scene):
    def construct(self):
        # Create the primary (front) green circle.
        circle1 = Circle(color=GREEN)
        circle1.move_to(ORIGIN)

        # Create the second green circle (we'll position it exactly at the same center).
        circle2 = Circle(color=GREEN)
        circle2.move_to(ORIGIN)

        # Animate the first circle appearing.
        self.play(Create(circle1), run_time=1)
        self.wait(0.5)

        # Animate the second circle appearing.
        # Since objects are drawn in the order they are added,
        # we add circle2 (even though its animation runs now) and then bring circle1 to the front.
        self.play(Create(circle2), run_time=1)
        self.bring_to_front(circle1)
        self.wait(0.5)

        # Draw a tick (check mark) on the first circle.
        # The tick is made of two line segments.
        tick_line1 = Line(LEFT * 0.3, ORIGIN)
        tick_line2 = Line(ORIGIN, RIGHT * 0.4 + UP * 0.4)
        tick = VGroup(tick_line1, tick_line2)
        tick.set_color(GREEN)
        tick.move_to(circle1.get_center())
        
        self.play(Create(tick), run_time=1)
        self.wait(1)
from manim import *

class FilledCircle(Scene):
    def construct(self):
        # TOTAL_TIME is the overall animation duration.
        TOTAL_TIME = 2
        # Our planned sum of durations is 1.5 sec (circles: 0.25*3, wait: 0.1, tick: 0.15*2, final wait: 0.35)
        base_total = 1.5  
        factor = TOTAL_TIME / base_total  # scale factor

        # Duration breakdown (original values)
        circle_duration = 0.25  # each circle's scale animation
        wait_after_circles = 0.1
        tick_duration = 0.15    # each tick segment
        final_wait = 0.35

        # Define colors (replace s_300, s_100, s_50 with your actual colors)
        dark_green = s_300    # darkest (front circle)
        medium_green = s_100  # medium (middle circle)
        light_green = s_50    # lightest (back circle)

        # Create circles (start tiny)
        back_circle = Circle(fill_color=light_green, fill_opacity=1)
        back_circle.set_stroke(width=0)
        back_circle.scale(0.01)

        middle_circle = Circle(fill_color=medium_green, fill_opacity=1)
        middle_circle.set_stroke(width=0)
        middle_circle.scale(0.01)

        front_circle = Circle(fill_color=dark_green, fill_opacity=1)
        front_circle.set_stroke(width=0)
        front_circle.scale(0.01)

        # Create the tick mark using two Lines with round caps
        tick_line1 = Line(
            start=LEFT * 0.3 + UP * 0.2,
            end=ORIGIN,
            stroke_width=14
        )
        tick_line1.set_cap_style(CapStyleType.ROUND)

        tick_line2 = Line(
            start=ORIGIN,
            end=RIGHT * 0.4 + UP * 0.6,
            stroke_width=14
        )
        tick_line2.set_cap_style(CapStyleType.ROUND)

        tick = VGroup(tick_line1, tick_line2)
        tick.set_color(WHITE)
        tick.move_to(front_circle.get_center())

        # Add circles (from back to front)
        self.add(back_circle, middle_circle, front_circle)

        # Animate circles growing sequentially with a smooth easing effect
        self.play(
            back_circle.animate.scale(200),
            run_time=circle_duration * factor,
            rate_func=rate_functions.ease_in_out_circ
        )
        self.play(
            middle_circle.animate.scale(150),
            run_time=circle_duration * factor,
            rate_func=rate_functions.ease_in_out_circ
        )
        self.play(
            front_circle.animate.scale(100),
            run_time=circle_duration * factor,
            rate_func=rate_functions.ease_in_out_circ
        )

        self.wait(wait_after_circles * factor)

        # Animate drawing the tick mark sequentially with the same easing
        self.play(
            Create(tick_line1),
            run_time=tick_duration * factor,
            rate_func=rate_functions.smooth
        )
        self.play(
            Create(tick_line2),
            run_time=tick_duration * factor,
            rate_func=rate_functions.smooth
        )

        self.wait(final_wait * factor)

class RoundedSquareFrame(Scene):
    def construct(self):
        # Define corner radius and frame size
        corner_radius = 0.5
        frame_size = 4  # Total width and height
        stroke_width = 8  # Thicker lines


        # Define corner arcs
        bottom_left_arc = Arc(radius=corner_radius, start_angle=PI, angle=PI/2).move_arc_center_to(DL * (frame_size / 2 - corner_radius) ).set_stroke(width=stroke_width).set_cap_style(CapStyleType.ROUND)
        top_left_arc = Arc(radius=corner_radius, start_angle=PI/2, angle=PI/2).move_arc_center_to(UL * (frame_size / 2 - corner_radius)).set_stroke(width=stroke_width).set_cap_style(CapStyleType.ROUND)
        top_right_arc = Arc(radius=corner_radius, start_angle=0, angle=PI/2).move_arc_center_to(UR * (frame_size / 2 - corner_radius)).set_stroke(width=stroke_width).set_cap_style(CapStyleType.ROUND)
        bottom_right_arc = Arc(radius=corner_radius, start_angle=-PI/2, angle=PI/2).move_arc_center_to(DR * (frame_size / 2 - corner_radius)).set_stroke(width=stroke_width).set_cap_style(CapStyleType.ROUND)

        self.play(Create(top_right_arc), run_time=0.25)
    
        self.play(Create(bottom_right_arc), run_time=0.25)
      
        self.play(Create(bottom_left_arc), run_time=0.25)
      
        self.play(Create(top_left_arc), run_time=0.25)

        self.wait()


class RoundedSquarestill(Scene):
    def construct(self):
        # Define corner radius and frame size
        corner_radius = 0.5
        frame_size = 4  # Total width and height
        stroke_width = 8  # Thicker lines

        # Define corner arcs
        bottom_left_arc = Arc(radius=corner_radius, start_angle=PI, angle=PI/2).move_arc_center_to(DL * (frame_size / 2 - corner_radius)).set_stroke(width=stroke_width).set_cap_style(CapStyleType.ROUND)
        top_left_arc = Arc(radius=corner_radius, start_angle=PI/2, angle=PI/2).move_arc_center_to(UL * (frame_size / 2 - corner_radius)).set_stroke(width=stroke_width).set_cap_style(CapStyleType.ROUND)
        top_right_arc = Arc(radius=corner_radius, start_angle=0, angle=PI/2).move_arc_center_to(UR * (frame_size / 2 - corner_radius)).set_stroke(width=stroke_width).set_cap_style(CapStyleType.ROUND)
        bottom_right_arc = Arc(radius=corner_radius, start_angle=-PI/2, angle=PI/2).move_arc_center_to(DR * (frame_size / 2 - corner_radius)).set_stroke(width=stroke_width).set_cap_style(CapStyleType.ROUND)

        arcs = VGroup(top_right_arc, bottom_right_arc, bottom_left_arc, top_left_arc)
        self.add(arcs)  # Display arcs immediately
        
        self.wait(1)  # Hold the scene for 1 second

class RoundedSquareToCheck(Scene):
    def construct(self):
        # Define corner radius and frame size
        corner_radius = 0.5
        frame_size = 4  # Total width and height
        stroke_width = 8  # Thicker lines

        # Define corner arcs
        bottom_left_arc = Arc(radius=corner_radius, start_angle=PI, angle=PI/2).move_arc_center_to(DL * (frame_size / 2 - corner_radius)).set_stroke(width=stroke_width).set_cap_style(CapStyleType.ROUND)
        top_left_arc = Arc(radius=corner_radius, start_angle=PI/2, angle=PI/2).move_arc_center_to(UL * (frame_size / 2 - corner_radius)).set_stroke(width=stroke_width).set_cap_style(CapStyleType.ROUND)
        top_right_arc = Arc(radius=corner_radius, start_angle=0, angle=PI/2).move_arc_center_to(UR * (frame_size / 2 - corner_radius)).set_stroke(width=stroke_width).set_cap_style(CapStyleType.ROUND)
        bottom_right_arc = Arc(radius=corner_radius, start_angle=-PI/2, angle=PI/2).move_arc_center_to(DR * (frame_size / 2 - corner_radius)).set_stroke(width=stroke_width).set_cap_style(CapStyleType.ROUND)

        arcs = VGroup(top_right_arc, bottom_right_arc, bottom_left_arc, top_left_arc)
        self.add(arcs)  # Display arcs immediately
        
        # Flickering effect
        for _ in range(5):  # Flicker for 5 seconds (approximately 5 cycles)
            self.play(FadeOut(arcs), run_time=0.35)
            self.play(FadeIn(arcs), run_time=0.35)

        # Transition: Fade out arcs and bring in circles
        self.play(FadeOut(arcs))

        # Define colors
        dark_green =  "#73EA69"  
        medium_green = "#B9F5B4"  
        light_green = "#DCFAD9" 
      

        # Create circles
        back_circle = Circle(fill_color=light_green, fill_opacity=1).set_stroke(width=0).scale(0.01)
        middle_circle = Circle(fill_color=medium_green, fill_opacity=1).set_stroke(width=0).scale(0.01)
        front_circle = Circle(fill_color=dark_green, fill_opacity=1).set_stroke(width=0).scale(0.01)

        # Create the tick mark
        tick_line1 = Line(start=LEFT * 0.3 + UP * 0.2, end=ORIGIN, stroke_width=14).set_cap_style(CapStyleType.ROUND)
        tick_line2 = Line(start=ORIGIN, end=RIGHT * 0.4 + UP * 0.6, stroke_width=14).set_cap_style(CapStyleType.ROUND)
        tick = VGroup(tick_line1, tick_line2).set_color(WHITE)
        tick.move_to(front_circle.get_center())

        # Add circles (from back to front)
        self.add(back_circle, middle_circle, front_circle)

        # Animate circles growing sequentially
        self.play(back_circle.animate.scale(200), run_time=0.25, rate_func=rate_functions.ease_in_out_circ)
        self.play(middle_circle.animate.scale(150), run_time=0.25, rate_func=rate_functions.ease_in_out_circ)
        self.play(front_circle.animate.scale(100), run_time=0.25, rate_func=rate_functions.ease_in_out_circ)

        self.wait(0.1)

        # Animate drawing the tick mark
        self.play(Create(tick_line1), run_time=0.15, rate_func=rate_functions.smooth)
        self.play(Create(tick_line2), run_time=0.15, rate_func=rate_functions.smooth)

        self.wait(0.35)


class ArcToFilledCircleAndTick_ImmediateTransform(Scene):
    def construct(self):
        # Parameters & Colors
        corner_radius = 0.5
        frame_size = 6
        stroke_width = 8
        s_300 = "#1b5e20"  # dark green (front circle)
        s_100 = "#388e3c"  # medium green (middle circle)
        s_50  = "#81c784"  # light green (back circle)

        TOTAL_TIME = 2
        base_total = 1.5  
        factor = TOTAL_TIME / base_total  
        circle_duration = 0.25  
        tick_duration = 0.15     

        # Create the Four Arcs
        bottom_left_arc = Arc(
            radius=corner_radius, start_angle=PI, angle=PI/2
        ).move_arc_center_to(DL * (frame_size/2 - corner_radius))\
         .set_stroke(width=stroke_width)\
         .set_cap_style(CapStyleType.ROUND)

        top_left_arc = Arc(
            radius=corner_radius, start_angle=PI/2, angle=PI/2
        ).move_arc_center_to(UL * (frame_size/2 - corner_radius))\
         .set_stroke(width=stroke_width)\
         .set_cap_style(CapStyleType.ROUND)

        top_right_arc = Arc(
            radius=corner_radius, start_angle=0, angle=PI/2
        ).move_arc_center_to(UR * (frame_size/2 - corner_radius))\
         .set_stroke(width=stroke_width)\
         .set_cap_style(CapStyleType.ROUND)

        bottom_right_arc = Arc(
            radius=corner_radius, start_angle=-PI/2, angle=PI/2
        ).move_arc_center_to(DR * (frame_size/2 - corner_radius))\
         .set_stroke(width=stroke_width)\
         .set_cap_style(CapStyleType.ROUND)

        self.add(bottom_left_arc, top_left_arc, top_right_arc, bottom_right_arc)
        self.wait(4)  # Wait for 4 seconds before starting the transformation

        # Helper: Vortex move with immediate transformation upon reaching center.
        def vortex_transform_immediate(arc, final_mobject, move_run_time=0.3, transform_run_time=0.5):
            path = ArcBetweenPoints(arc.get_center(), ORIGIN, angle=PI/6)
            self.play(MoveAlongPath(arc, path),
                      run_time=move_run_time,
                      rate_func=rate_functions.ease_in_out_circ)
            self.play(ReplacementTransform(arc, final_mobject),
                      run_time=transform_run_time)

        # Top-right arc → back circle.
        back_circle = Circle(fill_color=s_50, fill_opacity=1).set_stroke(width=0)
        back_circle.scale(0.01)
        vortex_transform_immediate(top_right_arc, back_circle, move_run_time=0.3, transform_run_time=0.5)
        self.play(back_circle.animate.scale(200),
                  run_time=circle_duration * factor,
                  rate_func=rate_functions.ease_in_out_circ)

        # Bottom-right arc → middle circle.
        middle_circle = Circle(fill_color=s_100, fill_opacity=1).set_stroke(width=0)
        middle_circle.scale(0.01)
        vortex_transform_immediate(bottom_right_arc, middle_circle, move_run_time=0.3, transform_run_time=0.5)
        self.play(middle_circle.animate.scale(150),
                  run_time=circle_duration * factor,
                  rate_func=rate_functions.ease_in_out_circ)

        # Bottom-left arc → front circle.
        front_circle = Circle(fill_color=s_300, fill_opacity=1).set_stroke(width=0)
        front_circle.scale(0.01)
        self.bring_to_front(front_circle)
        vortex_transform_immediate(bottom_left_arc, front_circle, move_run_time=0.3, transform_run_time=0.5)
        self.play(front_circle.animate.scale(100),
                  run_time=circle_duration * factor,
                  rate_func=rate_functions.ease_in_out_circ)

        # Top-left arc → tick mark.
        tick_line1 = Line(start=LEFT * 0.3 + UP * 0.2, end=ORIGIN, stroke_width=14)\
            .set_cap_style(CapStyleType.ROUND)
        tick_line2 = Line(start=ORIGIN, end=RIGHT * 0.4 + UP * 0.6, stroke_width=14)\
            .set_cap_style(CapStyleType.ROUND)
        tick = VGroup(tick_line1, tick_line2).set_color(WHITE)
        self.bring_to_front(tick)
        tick.move_to(front_circle.get_center())
        vortex_transform_immediate(top_left_arc, tick, move_run_time=0.3, transform_run_time=0.5)
        self.play(Create(tick_line1), run_time=tick_duration * factor, rate_func=rate_functions.smooth)
        self.play(Create(tick_line2), run_time=tick_duration * factor, rate_func=rate_functions.smooth)
        self.wait(0.35 * factor)
