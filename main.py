from window import Window, Point, Line

if __name__ == "__main__":
    # Create a window
    window = Window(height=600, width=800)

    # Create some points
    p1 = Point(100, 100)
    p2 = Point(200, 200)
    p3 = Point(200, 100)
    p4 = Point(100, 200)

    # Create some lines
    line1 = Line(p1, p2)
    line2 = Line(p3, p4)

    # Draw the lines on the window
    window.draw_line(line1, "red")
    window.draw_line(line2, "blue")

    # Keep the window open until closed by user
    window.wait_for_close()