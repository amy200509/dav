# ============================================================
# EXPERIMENT 2: Data Analytics Libraries in R
# Run this file directly in RStudio
# ============================================================

# ---------- Install packages (run once) ----------
# install.packages(c("dplyr","ggplot2","tidyr","readr",
#                    "stringr","lubridate","caret","corrplot"))

# ---------- 1. BASE R ----------
cat("--- Base R ---\n")
x <- c(10, 20, 30, 40, 50)
cat("Vector x:", x, "\n")
cat("Mean:", mean(x), "\n")
cat("Median:", median(x), "\n")
cat("Std Dev:", sd(x), "\n")
cat("Summary:\n")
print(summary(x))

# ---------- 2. DATA FRAME ----------
cat("\n--- Data Frame ---\n")
df <- data.frame(
  Name       = c("Alice", "Bob", "Charlie", "Diana"),
  Age        = c(25, 30, 35, 28),
  Salary     = c(50000, 60000, 70000, 55000),
  Department = c("HR", "IT", "Finance", "IT")
)
print(df)
cat("\nSummary:\n")
print(summary(df))
cat("Dimensions:", dim(df), "\n")
cat("Column Names:", names(df), "\n")

# ---------- 3. dplyr ----------
library(dplyr)
cat("\n--- dplyr ---\n")

cat("Filter Salary > 55000:\n")
print(filter(df, Salary > 55000))

cat("\nSelect Name & Salary:\n")
print(select(df, Name, Salary))

cat("\nArrange by Salary descending:\n")
print(arrange(df, desc(Salary)))

df <- mutate(df, Bonus = Salary * 0.10)
cat("\nAfter adding Bonus:\n")
print(df)

cat("\nGroup by Department - Mean Salary:\n")
print(df %>% group_by(Department) %>% summarise(Avg_Salary = mean(Salary)))

# ---------- 4. ggplot2 ----------
library(ggplot2)
cat("\n--- ggplot2 ---\n")

# Bar Chart
p1 <- ggplot(df, aes(x=Name, y=Salary, fill=Department)) +
  geom_bar(stat="identity") +
  ggtitle("Salary by Employee") +
  theme_minimal()
print(p1)

# Scatter Plot
p2 <- ggplot(df, aes(x=Age, y=Salary, color=Department)) +
  geom_point(size=4) +
  geom_smooth(method="lm", se=FALSE) +
  ggtitle("Age vs Salary") +
  theme_minimal()
print(p2)

# Histogram
p3 <- ggplot(df, aes(x=Salary)) +
  geom_histogram(binwidth=5000, fill="steelblue", color="black") +
  ggtitle("Salary Distribution") +
  theme_minimal()
print(p3)

# Boxplot
p4 <- ggplot(df, aes(x=Department, y=Salary, fill=Department)) +
  geom_boxplot() +
  ggtitle("Salary by Department") +
  theme_minimal()
print(p4)

# ---------- 5. tidyr ----------
library(tidyr)
cat("\n--- tidyr ---\n")

df_long <- pivot_longer(df, cols=c(Salary, Bonus),
                        names_to="Type", values_to="Amount")
cat("Pivot Longer:\n")
print(df_long)

# ---------- 6. readr ----------
library(readr)
cat("\n--- readr ---\n")
write_csv(df, "exp2_data.csv")
cat("CSV saved: exp2_data.csv\n")
df_read <- read_csv("exp2_data.csv")
cat("CSV read back:\n")
print(df_read)

# ---------- 7. stringr ----------
library(stringr)
cat("\n--- stringr ---\n")
names_vec <- c("Alice Smith", "Bob Jones", "Charlie Brown")
cat("Uppercase:", str_to_upper(names_vec), "\n")
cat("Contains Bob:", str_detect(names_vec, "Bob"), "\n")
cat("Replace Smith->Doe:", str_replace(names_vec, "Smith", "Doe"), "\n")

# ---------- 8. lubridate ----------
library(lubridate)
cat("\n--- lubridate ---\n")
cat("Today:", format(today()), "\n")
cat("Year:", year(today()), "\n")
cat("Month:", month(today()), "\n")
d1 <- ymd("2024-01-01")
d2 <- ymd("2024-12-31")
cat("Days between:", as.numeric(d2 - d1), "\n")

# ---------- 9. corrplot ----------
library(corrplot)
cat("\n--- corrplot ---\n")
num_df <- df[, c("Age", "Salary", "Bonus")]
corr_matrix <- cor(num_df)
cat("Correlation Matrix:\n")
print(round(corr_matrix, 2))
corrplot(corr_matrix, method="color", addCoef.col="black",
         title="Correlation Matrix", mar=c(0,0,1,0))

cat("\n========================================\n")
cat("Experiment 2 Complete!\n")
cat("========================================\n")
