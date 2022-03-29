# COMPETITIONS-IN-DATA-SCIENCES

## app.py若是無法執行，可以使用colab直接運行
colab:https://colab.research.google.com/drive/12RbTWodnvuYtnWZW1CkcKHIdkeGF6Nsp?usp=sharing

### preprocessing
- 在網頁上下載了兩個csv檔，分別是"本年度每日尖峰備轉容量率"與"近三年每日尖峰備轉容量率"。
- 兩份資料的範圍分別是[2019-1-1,2021-12-31]，[2022-1-1,2022-3-28]
- 資料僅包含"日期"，"備轉容量(MW)"，"備轉容量率(%)"。
- 將兩個檔案做串接後，觀察分布曲線。
![資料圖片](https://user-images.githubusercontent.com/37070545/160620968-70dff37f-dff9-4a67-b490-1fb0f8a16e18.png)
### data
- 取出資料中1，2，3，4月當作訓練資料
- 將資料調整成模型需要的輸入格式
### training
- 這次使用的是FB的Prophet，或稱“Facebook Prophet”，是一個由Facebook開發的用於單變數時間序列預測的開源庫。
- Prophet實現的是一個可加的時間序列預測模型，支援趨勢、季節性週期變化及節假日效應。
- “該模型所實現的是一個基於可加模型的時間序列資料預測過程，擬合了年度、周度、日度的季節性週期變化及節假日效應的非線性趨勢。” — Package ‘prophet’, 2019.
### result
- 黑色的點是實際的值，而藍色的線是模型預測的值，而淺藍色的範圍是模型預測的上下限。
![預測圖](https://user-images.githubusercontent.com/37070545/160627855-1cd3ce08-abf9-4963-bdbc-15b7e5092ebc.png)
### testing
- 在以往測試時，曾經利用模型預測最後14天的資料
- 得到了RMSE為500左右的成績
![預測曲線](https://user-images.githubusercontent.com/37070545/160628258-feba7d9f-6010-4061-904d-3b59ed73d931.png)
