def stream_batches(data,size):
    batch=[]
    for x in data:
        batch.append(x)
        if len(batch)==size:
            yield batch
            batch=[]
    if batch:
        yield batch
data=[1,2,3,4,5,6,7,8]
print(list(stream_batches(data,3)))