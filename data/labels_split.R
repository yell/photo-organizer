train <- read.csv("train_labels.csv", header = T)
test <- read.csv("test_labels.csv", header = T)

train <- as.data.frame(cbind("photo_name" = substr(train[,1], 1, 13), "label" = as.numeric(substr(train[,1], 15, 17))))
test <- as.data.frame(cbind("photo_name" = substr(test[,1], 1, 13), "label" = as.numeric(substr(test[,1], 15, 17))))

x <- as.data.frame(table(train[,2]))
y <- as.data.frame(table(test[,2]))

library(ggplot2)
ssx = sum(x[,2])
ssy = sum(y[,2])
ggplot(data = x, (aes(x = Var1, y = Freq))) + geom_bar(stat="identity") + ggtitle("Train Labels Split, %")+ 
  geom_text(aes(label=round(100*Freq/ssx, 2), vjust=0))

ggplot(data = y, (aes(x = Var1, y = Freq))) + geom_bar(stat="identity") + ggtitle("Test Labels Split, %")+ 
  geom_text(aes(label=round(100*Freq/ssy, 2), vjust=0))
