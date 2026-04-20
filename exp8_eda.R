# ============================================================
# EXPERIMENT 8: Exploratory Data Analysis (EDA) in R
# na, summary, plot, hist, boxplot
# Run this file directly in RStudio
# ============================================================

cat("========================================\n")
cat("EXPERIMENT 8: EDA in R\n")
cat("========================================\n")

# ---------- Create Dataset ----------
Name   <- c("Alice","Bob","Charlie","Diana","Eve","Frank","Grace","Hank","Ivy","Jack","Karen","Leo")
Age    <- c(23, 25, NA, 30, 32, 35, 28, NA, 40, 22, 27, 33)
Salary <- c(30000,35000,40000,NA,50000,60000,45000,55000,70000,28000,38000,52000)
Score  <- c(88, 76, 92, 85, NA, 78, 90, 82, 95, 70, 88, 79)
Dept   <- c("HR","IT","HR","IT","Finance","Finance","IT","HR","Finance","IT","HR","Finance")

df <- data.frame(Name, Age, Salary, Score, Dept, stringsAsFactors=FALSE)

cat("\n--- Raw Dataset ---\n")
print(df)

# ---------- Check Missing Values (is.na) ----------
cat("\n--- Missing Values (is.na) ---\n")
print(is.na(df))
cat("\nCount of NA per column:\n")
print(colSums(is.na(df)))

# ---------- Handle Missing Values ----------
df$Age[is.na(df$Age)]       <- mean(df$Age, na.rm=TRUE)
df$Salary[is.na(df$Salary)] <- median(df$Salary, na.rm=TRUE)
df$Score[is.na(df$Score)]   <- mean(df$Score, na.rm=TRUE)

cat("\nAfter handling NA:\n")
print(df)

# ---------- Summary ----------
cat("\n--- Summary ---\n")
print(summary(df))

# ---------- Structure ----------
cat("\n--- Structure (str) ---\n")
str(df)

# ---------- hist() - Histograms ----------
cat("\n--- Histograms ---\n")
par(mfrow=c(1,3))  # 3 plots in one row

hist(df$Age,
     main="Histogram: Age",
     xlab="Age",
     col="skyblue",
     border="black",
     breaks=6)

hist(df$Salary,
     main="Histogram: Salary",
     xlab="Salary",
     col="salmon",
     border="black",
     breaks=6)

hist(df$Score,
     main="Histogram: Score",
     xlab="Score",
     col="lightgreen",
     border="black",
     breaks=6)

par(mfrow=c(1,1))  # reset layout

# ---------- boxplot() ----------
cat("\n--- Boxplots ---\n")
par(mfrow=c(1,3))

boxplot(df$Age,
        main="Boxplot: Age",
        col="skyblue",
        ylab="Age")

boxplot(df$Salary,
        main="Boxplot: Salary",
        col="salmon",
        ylab="Salary")

boxplot(df$Score,
        main="Boxplot: Score",
        col="lightgreen",
        ylab="Score")

par(mfrow=c(1,1))

# Boxplot by group
boxplot(Salary ~ Dept,
        data=df,
        main="Salary by Department",
        col=c("lightblue","lightpink","lightyellow"),
        xlab="Department",
        ylab="Salary")

# ---------- plot() ----------
cat("\n--- plot() ---\n")
plot(df$Age, df$Salary,
     main="Age vs Salary",
     xlab="Age",
     ylab="Salary",
     col="purple",
     pch=16,
     cex=1.5)
abline(lm(Salary ~ Age, data=df), col="red", lwd=2)

# ---------- Bar Plot ----------
cat("\n--- Bar Plot: Department Count ---\n")
dept_table <- table(df$Dept)
print(dept_table)
barplot(dept_table,
        main="Department Count",
        col=c("lightblue","lightpink","lightyellow"),
        xlab="Department",
        ylab="Count")

# ---------- Pie Chart ----------
cat("\n--- Pie Chart ---\n")
pie(dept_table,
    main="Department Distribution",
    col=c("lightblue","lightpink","lightyellow"))

# ---------- Correlation ----------
cat("\n--- Correlation ---\n")
num_cols <- df[, c("Age","Salary","Score")]
print(cor(num_cols))

cat("\n========================================\n")
cat("Experiment 8 Complete!\n")
cat("========================================\n")
