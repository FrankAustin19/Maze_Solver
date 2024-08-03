from window import Window, Cell, Maze

if __name__ == "__main__":
    # Create a window
    window = Window(height=600, width=800)

    # Create a maze
    maze = Maze(x1=10, y1=10, num_rows=5, num_cols=5, cell_size_x=30, cell_size_y=30, win=window)

    # Optional: Print some information about the maze cells for verification
    for i in range(len(maze._cells)):
        for j in range(len(maze._cells[i])):
            cell = maze._cells[i][j]
            print(f"Cell[{i}][{j}] -> Position: (({cell.x1}, {cell.y1}), ({cell.x2}, {cell.y2}))")

    # Keep the window open until closed by user
    window.wait_for_close()