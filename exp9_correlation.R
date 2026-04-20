# ============================================================
# EXPERIMENT 9: Correlation & Multi-Variable Analysis in R
# Run this file directly in RStudio
# ============================================================

# ---------- Install if needed ----------
# install.packages(c("ggplot2", "corrplot", "GGally"))

cat("========================================\n")
cat("EXPERIMENT 9: Correlation & Multi-Variable Analysis\n")
cat("========================================\n")

# ---------- Dataset ----------
set.seed(42)
n <- 50
df <- data.frame(
  Age        = sample(22:55, n, replace=TRUE),
  Experience = sample(1:30,  n, replace=TRUE),
  Salary     = sample(30000:100000, n, replace=TRUE),
  Score      = sample(60:100, n, replace=TRUE),
  Hours_Work = sample(30:60,  n, replace=TRUE)
)

cat("\nDataset Head:\n")
print(head(df))

cat("\nSummary:\n")
print(summary(df))

# ---------- Correlation Matrix ----------
cat("\n--- Correlation Matrix ---\n")
corr_matrix <- cor(df)
print(round(corr_matrix, 2))

# ---------- corrplot - Heatmap ----------
library(corrplot)
cat("\n--- Correlation Heatmap (corrplot) ---\n")
corrplot(corr_matrix,
         method  = "color",
         addCoef.col = "black",
         tl.col  = "black",
         title   = "Correlation Heatmap",
         mar     = c(0,0,1,0))

# Circular style
corrplot(corr_matrix,
         method = "circle",
         type   = "upper",
         tl.col = "black",
         title  = "Correlation Circle Plot",
         mar    = c(0,0,1,0))

# ---------- Scatter Plots ----------
cat("\n--- Scatter Plots ---\n")
par(mfrow=c(1,3))

plot(df$Age, df$Salary,
     main="Age vs Salary",
     xlab="Age", ylab="Salary",
     col="blue", pch=16)
abline(lm(Salary ~ Age, data=df), col="red", lwd=2)

plot(df$Experience, df$Salary,
     main="Experience vs Salary",
     xlab="Experience", ylab="Salary",
     col="green", pch=16)
abline(lm(Salary ~ Experience, data=df), col="red", lwd=2)

plot(df$Hours_Work, df$Score,
     main="Hours Work vs Score",
     xlab="Hours Work", ylab="Score",
     col="purple", pch=16)
abline(lm(Score ~ Hours_Work, data=df), col="red", lwd=2)

par(mfrow=c(1,1))

# ---------- Pairs Plot (Scatter Matrix) ----------
cat("\n--- Pairs Plot ---\n")
pairs(df,
      main  = "Scatter Matrix - All Variables",
      col   = "steelblue",
      pch   = 16,
      cex   = 0.8)

# ---------- GGally pairplot (ggplot2 style) ----------
library(GGally)
ggpairs(df,
        title = "GGally Pair Plot") +
  theme_minimal()

# ---------- ggplot2 Visualizations ----------
library(ggplot2)
cat("\n--- ggplot2 Visualizations ---\n")

# Scatter with trend
p1 <- ggplot(df, aes(x=Age, y=Salary)) +
  geom_point(color="steelblue", size=2, alpha=0.7) +
  geom_smooth(method="lm", color="red", se=TRUE) +
  ggtitle("Age vs Salary with Regression Line") +
  theme_minimal()
print(p1)

# Multi-variable scatter
p2 <- ggplot(df, aes(x=Experience, y=Salary, size=Score, color=Hours_Work)) +
  geom_point(alpha=0.7) +
  scale_color_gradient(low="blue", high="red") +
  ggtitle("Experience vs Salary (Size=Score, Color=Hours)") +
  theme_minimal()
print(p2)

# ---------- Grouped Bar Chart ----------
cat("\n--- Department Analysis ---\n")
dept_df <- data.frame(
  Dept   = c("HR","IT","Finance","HR","IT","Finance"),
  Salary = c(45000,70000,60000,40000,75000,55000),
  Score  = c(80,90,85,75,88,82)
)
dept_avg <- aggregate(. ~ Dept, data=dept_df, FUN=mean)
cat("Department Averages:\n")
print(dept_avg)

# Reshape for grouped bar
dept_long <- tidyr::pivot_longer(dept_avg,
                                  cols=c(Salary, Score),
                                  names_to="Metric",
                                  values_to="Value")

p3 <- ggplot(dept_long, aes(x=Dept, y=Value, fill=Metric)) +
  geom_bar(stat="identity", position="dodge") +
  ggtitle("Average Salary & Score by Department") +
  theme_minimal()
print(p3)

# ---------- cor.test (significance) ----------
cat("\n--- Correlation Significance Test ---\n")
cat("Age vs Salary:\n")
print(cor.test(df$Age, df$Salary))

cat("\nExperience vs Salary:\n")
print(cor.test(df$Experience, df$Salary))

cat("\n========================================\n")
cat("Experiment 9 Complete!\n")
cat("========================================\n")
