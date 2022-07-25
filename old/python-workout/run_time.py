
def run_timing():
    cnt = 0
    total_time = 0
    while True:
        input_time = input('Enter 10km run time: ')

        if not input_time:
            break

        total_time += float(input_time)
        cnt += 1

    average_time = total_time / cnt  
    print(f'Average of {average_time}, over {cnt} runs')

run_timing()
        