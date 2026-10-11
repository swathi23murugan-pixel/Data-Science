from abc import ABC,abstractmethod
class BaseDataTransformer(ABC):
    @abstractmethod
    def transform(self,data):
        pass
class NormalizerTransformer(BaseDataTransformer):
    def transform(self,data):
        m=max(data)
        return [round(x/m,2) for x in data]
class StandardizerTransformer(BaseDataTransformer):
    def transform(self,data):
        mean=sum(data)/len(data)
        std=(sum((x-mean)**2 for x in data)/len(data))**0.5
        return [round((x-mean)/std,2) for x in data]
norm=NormalizerTransformer()
std=StandardizerTransformer()
print("Normalized :",norm.transform([10,20,50,100]))
print("Standardized:",std.transform([10,20,30,40,50]))