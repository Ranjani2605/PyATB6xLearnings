class BaseCounter:

     count = 0

     def test_execution(self):
         BaseCounter.count += 1
         return BaseCounter.count





obj_basecounter = BaseCounter()
print(obj_basecounter.test_execution())
print(obj_basecounter.test_execution())
