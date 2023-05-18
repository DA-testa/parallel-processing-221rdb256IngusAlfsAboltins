mport heapq

def parallel_processing(n, m, data):

    threads = [(0, i) for i in range(n)]

    jobq = [(job, i) for i, job in enumerate(data)]

    output = []
    

    while jobq:
       
        job, job_index = heapq.heappop(job_queue)
      
        start_time, thread_index = heapq.heappop(threads)

        output.append((thread_index, start_time))
      
        finish_time = start_time + job

        heapq.heappush(threads, (finish_time, thread_index))
        
    return output

def main():

    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)
    
  
    for thread_index, start_time in result:
        print(thread_index, start_time)

if __name__ == "__main__":
    main()
