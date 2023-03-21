import heapq

def parallel_processing(n, m, data):

    workers = [(0, i) for i in range(n)]

    job_queue = [(job, i) for i, job in enumerate(data)]

    output = []
    

    while job_queue:
       
        job, job_index = heapq.heappop(job_queue)
      
        start_time, worker_index = heapq.heappop(workers)

        output.append((worker_index, start_time))
      
        finish_time = start_time + job

        heapq.heappush(workers, (finish_time, worker_index))
        
    return output

def main():

    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)
    
  
    for worker_index, start_time in result:
        print(worker_index, start_time)

if __name__ == "__main__":
    main()
