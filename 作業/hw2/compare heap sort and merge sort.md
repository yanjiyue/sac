# Heap sort 與 Merge sort的比較
參考老師moodle上的表，如下
![Image text](https://github.com/yanjiyue/leecode/blob/master/h%20und%20m/1.png)
以下為來自[https://blog.csdn.net/microsues/article/details/6107584的表格](https://blog.csdn.net/microsues/article/details/6107584的表格)
![Image text](https://github.com/yanjiyue/leecode/blob/master/h%20und%20m/2.png)
可見兩種sort的速度雖然是同一個階層的，但是merge sort佔用的空間更大，由於merge sort需要分塊後比較的緣故，所以需要佔用更多空間，而heap sort則是一個root跟各個子節點比較，並不需要佔用多餘空間，故佔用空間較小；
##
但穩定性上看，則merge sort更優，或許是由於分法比較簡單，由兩數之間比較慢慢發展為兩個大list比較，比較相對簡單；而heap sort的root則需時常變更的緣故吧。
##
另一方面看，merge sort像組團後比較，而heap sort比較像單點比較，直覺上merge sort也比heap sort來的穩定
##
從他們的長相上看，merge sort為{a,b,c,d,e},Heap sort為![Image text](https://github.com/yanjiyue/leecode/blob/master/h%20und%20m/3.png)
看上去，merge sort也給人比較穩定的感覺
##
總的來說，merge sort比heap sort的優勢是穩定，而heap sort比merge sort的優勢在於節省空間
##
所以如果資料量過大的情況下，比較適用heap sort；
而在資料量較小且追求穩定性的情況下，比較適用merge sort。
##
* 參考資料
1、[https://blog.csdn.net/microsues/article/details/6107584](https://blog.csdn.net/microsues/article/details/6107584)
2、[https://docs.google.com/presentation/d/e/2PACX-1vRAGwnUvg6BcXoML5u9f4gO6YKcz0vXf7bDnPho_S7mG5D0SBR78djt91RKUPMxqNfkVIcu3l5WCXPh/pub?start=false&loop=false&delayms=3000&slide=id.g6504c48e6e_0_6](https://docs.google.com/presentation/d/e/2PACX-1vRAGwnUvg6BcXoML5u9f4gO6YKcz0vXf7bDnPho_S7mG5D0SBR78djt91RKUPMxqNfkVIcu3l5WCXPh/pub?start=false&loop=false&delayms=3000&slide=id.g6504c48e6e_0_6)
3、[https://tingtseng.pixnet.net/blog/post/39924871-algorithm-time-complexity-演算法時間複雜度整理](https://tingtseng.pixnet.net/blog/post/39924871-algorithm-time-complexity-演算法時間複雜度整理)
