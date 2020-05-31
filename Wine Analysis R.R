#Camila Kosma 24/05/2020

library(leaps)
library(ggplot2)
library(reshape2)
library(MASS)
library(ggcorrplot)
library(plotmo)
library(rpart)
library(rpart.plot)
library(tidyverse)
library(corrplot)
library(gridExtra)
library(GGally)
library(knitr)

#Get the dataset from URL
red_data <- read.csv("https://query.data.world/s/uwnbkixzuarlyb7kvtighli2okv7kn")
white_data <- read.csv("https://query.data.world/s/nhgaqjqexeir27sqdc7ordwmuaikhu")

#Data Preparation
str(red_data)
str(white_data)

head(red_data)
head(white_data)

summary(red_data)
summary(white_data)

sapply(red_data, sd)
sapply(white_data, sd)

df <- scale(red_data[-1])
head(df)
df <- scale(white_data[-1])
head(df)

#Histogram of Quality in a first place
hist(red_data$quality)
hist(white_data$quality)

#Training, Test set and graphics outputs
red_wine_train <- red_data[1:3750, ]
red_wine_test <- red_data[3751:4898, ]
white_wine_train <- white_data[1:3750, ]
white_wine_test <- white_data[3751:4898, ]


red_m.rpart <- rpart(quality ~ ., data = red_wine_train)
red_m.rpart
white_m.rpart <- rpart(quality ~ ., data = white_wine_train)
white_m.rpart


rpart.plot(red_m.rpart, digits = 3)
rpart.plot(white_m.rpart, digits = 3)

rpart.plot(red_m.rpart, digits = 4, fallen.leaves = TRUE, type = 3, extra = 101)
rpart.plot(white_m.rpart, digits = 4, fallen.leaves = TRUE, type = 3, extra = 101)

red_p.rpart <- predict(red_m.rpart, red_wine_test)
summary(red_p.rpart)
white_p.rpart <- predict(white_m.rpart, white_wine_test)
summary(white_p.rpart)

#Boxplot Wine Attributes
red_oldpar = par(mfrow = c(2,6))
for ( i in 1:11 ) {
  boxplot(red_data[[i]])
  mtext(names(red_data)[i], cex = 0.8, side = 1, line = 2)
}
par(red_oldpar)

white_oldpar = par(mfrow = c(2,6))
for ( i in 1:11 ) {
  boxplot(white_data[[i]])
  mtext(names(white_data)[i], cex = 0.8, side = 1, line = 2)
}
par(white_oldpar)

corrplot(cor(red_data), type="upper", method="ellipse", tl.cex=0.9)

#Classification of Quality
hist(red_data$quality)
hist(white_data$quality)

red_data$taste <- ifelse(red_data$quality < 6, 'poor', 'high')
red_data$taste[red_data$quality == 6] <- 'standard'
red_data$taste <- as.factor(red_data$taste)
table(red_data$taste)
white_data$taste <- ifelse(white_data$quality < 6, 'poor', 'high')
white_data$taste[white_data$quality == 6] <- 'standard'
white_data$taste <- as.factor(white_data$taste)
table(white_data$taste)

#Correlation Matrix
corrplot(cor(red_data), type="upper", method="ellipse", tl.cex=0.9)

#Relation between 2 variables
ggplot(red_data, aes(x=Acidity, y=Sulphur)) +
  geom_point() +
  geom_smooth(method="lm", se=FALSE) +
  labs(title="Wines Attributes",
       subtitle="Relationship between Phenols and Flavanoids") +
  theme_bw()








