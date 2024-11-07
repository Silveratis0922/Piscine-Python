def ft_tqdm(lst: range) -> None:
    """
    Displays a progress bar while iterating over the given range.
    """
    total = len(lst)
    length = 50
    fill = '█'

    def print_progress(iteration):
        """
        Updates and displays the progress bar based on the current iteration.
        """
        filled_length = int(length * iteration // total)
        bar = fill * filled_length + ' ' * (length - filled_length)
        percent = (int)((iteration / total) * 100)
        print(f'\r {percent}%|{bar}| {iteration}/{total}', end='')

    print_progress(0)

    for i, item in enumerate(lst):
        print_progress(i + 1)
        yield item
    print()
