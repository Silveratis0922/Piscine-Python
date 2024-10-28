def ft_tqdm(lst: range) -> None:
    total = len(lst)
    length = 50
    fill = '█'

    def print_progress(iteration):
        filled_length = int(length * iteration // total)
        bar = fill * filled_length + ' ' * (length - filled_length)
        percent = (int)((iteration / total) * 100)
        print(f'\r {percent}%|{bar}| {iteration}/{total}', end='')

    print_progress(0)

    for i, item in enumerate(lst):
        print_progress(i + 1)
        yield item
    print()
