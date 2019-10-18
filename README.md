# 資料結構與演算法
## 課程資料
* [linked list](https://docs.google.com/presentation/d/e/2PACX-1vTB218-EdUZ5jpNz6Uv4TOZQc37Y281v128_aRcWC6EhkTQs5bS8fh7yysmcuzb9R2QPN6_PDshFWL_/pub?start=false&loop=false&delayms=3000&slide=id.p)
* [stack&queue](https://docs.google.com/presentation/d/e/2PACX-1vQ1hb79im0vqpApCttGnXAFRT8SqH9HQP0b_oyVRCV8SVyiHLkHJjidYGAfxkvq468QMumFIDdTeiB-/pub?start=false&loop=false&delayms=3000&slide=id.p)
* [set](https://docs.google.com/presentation/d/e/2PACX-1vT6BvB7aI9oLgyum8tdIgGVr8kabqtwo8KZV3ayzKKQqGkpAnvrjT3JabWu-Hms9kUaDILyCU8-Qqhl/pub?start=false&loop=false&delayms=3000&slide=id.p)
* [insertion sort](https://docs.google.com/presentation/d/e/2PACX-1vQOTMDM-5-OUaGfnLUOFVgefFwSVRplSwnbicp0CXOQrB5H8RM_1Aq8o_4JxHlncEmhjvqk3tzcoB7s/pub?start=false&loop=false&delayms=3000&slide=id.p)
* [quick sort](https://docs.google.com/presentation/d/e/2PACX-1vSqz8sTxT4xyjgiz-htLvZd7FZ_5ZzgKf60pFEoNLU5S77JxrsGJ2vd15CdxlfLtT3g2aizHP-Ebk9b/pub?start=false&loop=false&delayms=3000&slide=id.p)
* [heap sort](https://docs.google.com/presentation/d/e/2PACX-1vRAGwnUvg6BcXoML5u9f4gO6YKcz0vXf7bDnPho_S7mG5D0SBR78djt91RKUPMxqNfkVIcu3l5WCXPh/pub?start=false&loop=false&delayms=3000&slide=id.p)

## 行事記錄
### week2 
* 做[design linklist](https://github.com/yanjiyue/sac/blob/master/%E7%B7%B4%E7%BF%92/design%20linked%20list.py)
---
### week3 
* 做[min stack](https://github.com/yanjiyue/sac/blob/master/%E7%B7%B4%E7%BF%92/min%20stack.py)與[implement queue using stacks](https://github.com/yanjiyue/sac/blob/master/%E7%B7%B4%E7%BF%92/Implement%20Queue%20using%20Stacks.py)
* 自學CS50
---
### week4
* 解釋[set mismatch](https://github.com/yanjiyue/sac/blob/master/%E7%B7%B4%E7%BF%92/set%20mismatch%E8%A7%A3%E9%87%8B)
* 自學CS50
---
### week5
* 做[quick sort](https://github.com/yanjiyue/sac/blob/master/%E4%BD%9C%E6%A5%AD/quicksort.ipynb)作業及[推導圖](https://github.com/yanjiyue/sac/blob/master/%E4%BD%9C%E6%A5%AD/quicksort.png)
---
### week6
* 完成[quick sort](https://github.com/yanjiyue/sac/blob/master/%E4%BD%9C%E6%A5%AD/quicksort.ipynb)作業及[推導圖](https://github.com/yanjiyue/sac/blob/master/%E4%BD%9C%E6%A5%AD/quicksort.png)
* 練習LeetCode，題目[Two Sum](https://github.com/yanjiyue/sac/blob/master/%E7%B7%B4%E7%BF%92/two%20sum.py)
* [Univalued Binary Tree](https://github.com/yanjiyue/sac/blob/master/%E7%B7%B4%E7%BF%92/Univalued%20Binary%20Tree.py)
---
### week7
### week8
### week9
### week10
### week11
### week12
### week13
### week14
### week15
### week16
### week17
### week18
---
---
## 筆記
### linked list
>prev指向前面節點|item數據|指向後面的節點
#### LinkedList 特點
 - 雙向鏈表實現
 - 元素時有序的，輸出順序與輸入順序一致
 - 允許元素為 null
 - 要找到某個結點，必須從頭開始遍曆。（查詢慢，增刪快）
 - 和 ArrayList 一樣，不是同步容器
---
### quick sort
>快速排序（Quicksort）是對冒泡排序的一種改進。它的基本思想是：通過一趟排序將要排序的數據分割成獨立的兩部分，其中一部分的所有數據都比另外一部分的所有數據都要小，然後再按此方法對這兩部分數據分別進行快速排序，整個排序過程可以遞歸進行，以此達到整個數據變成有序序列。
#### 排序流程
快速排序演算法通過多次比較和交換來實現排序，其排序流程如下： 
- 首先設定一個分界值，通過該分界值將數組分成左右兩部分。 
- 將大於或等於分界值的數據集中到數組右邊，小於分界值的數據集中到數組的左邊。此時，左邊部分中各元素都小於或等於分界值，而右邊部分中各元素都大於或等於分界值。 
- 然後，左邊和右邊的數據可以獨立排序。對於左側的數組數據，又可以取一個分界值，將該部分數據分成左右兩部分，同樣在左邊放置較小值，右邊放置較大值。右側的數組數據也可以做類似處理。 
- 重複上述過程，可以看出，這是一個遞歸定義。通過遞歸將左側部分排好序後，再遞歸排好右側部分的順序。當左、右兩個部分各數據排序完成後，整個數組的排序也就完成了。
#### 原理
設要排序的數組是A[0]……A[N-1]，首先任意選取一個數據（通常選用數組的第一個數）作為關鍵數據，然後將所有比它小的數都放到它左邊，所有比它大的數都放到它右邊，這個過程稱為一趟快速排序。值得注意的是，快速排序不是一種穩定的排序演算法，也就是說，多個相同的值的相對位置也許會在演算法結束時產生變動。
#### 一趟快速排序的演算法是：
- 設置兩個變數i、j，排序開始的時候：i=0，j=N-1； 
- 以第一個數組元素作為關鍵數據，賦值給key，即key=A[0]； 
- 從j開始向前搜索，即由後開始向前搜索(j--)，找到第一個小於key的值A[j]，將A[j]和A[i]的值交換； 
- 從i開始向後搜索，即由前開始向後搜索(i++)，找到第一個大於key的A[i]，將A[i]和A[j]的值交換；
- 重複第3、4步，直到i=j； (3,4步中，沒找到符合條件的值，即3中A[j]不小於key,4中A[i]不大於key的時候改變j、i的值，使得j=j-1，i=i+1，直至找到為止。找到符合條件的值，進行交換的時候i， j指針位置不變。另外，i==j這一過程一定正好是i+或j-完成的時候，此時令迴圈結束）。
---
### heap sort
>堆排序（英語：Heapsort）是指利用堆這種數據結構所設計的一種排序演算法。堆是一個近似完全二叉樹的結構，並同時滿足堆積的性質：即子結點的鍵值或索引總是小於（或者大於）它的父節點。
#### 堆的操作
在堆的數據結構中，堆中的最大值總是位於根節點（在優先佇列中使用堆的話堆中的最小值位於根節點）。堆中定義以下幾種操作：

- 最大堆調整（Max Heapify）：將堆的末端子節點作調整，使得子節點永遠小於父節點
- 創建最大堆（Build Max Heap）：將堆中的所有數據重新排序
- 堆排序（HeapSort）：移除位在第一個數據的根節點，並做最大堆調整的遞歸運算
---
