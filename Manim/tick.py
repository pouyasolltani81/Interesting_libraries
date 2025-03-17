from manim import *
s_300 = "#73EA69"
s_100 = "#B9F5B4"
s_50 = "#DCFAD9"
# manim -pql --gif beautiful_3d_circle.py Beautiful3DCircle

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
        TOTAL_TIME = 2.5
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
            start=LEFT * 0.4 + UP * 0.3,
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
            rate_func=rate_functions.smooth
        )
        self.play(
            middle_circle.animate.scale(150),
            run_time=circle_duration * factor,
            rate_func=rate_functions.smooth
        )
        self.play(
            front_circle.animate.scale(100),
            run_time=circle_duration * factor,
            rate_func=rate_functions.smooth
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
