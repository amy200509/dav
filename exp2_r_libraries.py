# ============================================================
# EXPERIMENT 2: Data Analytics Libraries in R
# (Demonstrated in Python with equivalent R code shown in comments)
# Run the R code in RStudio / R console
# ============================================================

# ============================================================
# >>>  R CODE  (copy-paste into RStudio to run)
# ============================================================
r_code = """
# ============================================================
# EXPERIMENT 2: Data Analytics Libraries in R
# ============================================================

# ---------- 1. BASE R ----------
cat("--- Base R ---\\n")
x <- c(10, 20, 30, 40, 50)
cat("Vector x:", x, "\\n")
cat("Mean:", mean(x), "\\n")
cat("Median:", median(x), "\\n")
cat("Std Dev:", sd(x), "\\n")
cat("Summary:\\n")
print(summary(x))

# ---------- 2. DATA FRAME (Base R) ----------
cat("\\n--- Data Frame ---\\n")
df <- data.frame(
  Name       = c("Alice", "Bob", "Charlie", "Diana"),
  Age        = c(25, 30, 35, 28),
  Salary     = c(50000, 60000, 70000, 55000),
  Department = c("HR", "IT", "Finance", "IT")
)
print(df)
cat("\\nSummary:\\n")
print(summary(df))
cat("\\nDimensions:", dim(df), "\\n")
cat("Column Names:", names(df), "\\n")

# ---------- 3. dplyr ----------
# install.packages("dplyr")
library(dplyr)
cat("\\n--- dplyr ---\\n")

# Filter
cat("Filter: Salary > 55000\\n")
print(filter(df, Salary > 55000))

# Select
cat("\\nSelect Name & Salary:\\n")
print(select(df, Name, Salary))

# Arrange
cat("\\nArrange by Salary (desc):\\n")
print(arrange(df, desc(Salary)))

# Mutate
df <- mutate(df, Bonus = Salary * 0.10)
cat("\\nAfter adding Bonus:\\n")
print(df)

# Summarise + Group By
cat("\\nGroup by Dept - Mean Salary:\\n")
print(df %>% group_by(Department) %>% summarise(Avg_Salary = mean(Salary)))

# ---------- 4. ggplot2 ----------
# install.packages("ggplot2")
library(ggplot2)
cat("\\n--- ggplot2 ---\\n")

# Bar Chart
p1 <- ggplot(df, aes(x=Name, y=Salary, fill=Department)) +
  geom_bar(stat="identity") +
  ggtitle("Salary by Employee") +
  theme_minimal()
print(p1)
ggsave("exp2_barchart.png", plot=p1)

# Scatter Plot
p2 <- ggplot(df, aes(x=Age, y=Salary, color=Department)) +
  geom_point(size=4) +
  geom_smooth(method="lm", se=FALSE) +
  ggtitle("Age vs Salary") +
  theme_minimal()
print(p2)
ggsave("exp2_scatter.png", plot=p2)

# Histogram
p3 <- ggplot(df, aes(x=Salary)) +
  geom_histogram(binwidth=5000, fill="steelblue", color="black") +
  ggtitle("Salary Distribution") +
  theme_minimal()
print(p3)
ggsave("exp2_histogram.png", plot=p3)

# Boxplot
p4 <- ggplot(df, aes(x=Department, y=Salary, fill=Department)) +
  geom_boxplot() +
  ggtitle("Salary by Department - Boxplot") +
  theme_minimal()
print(p4)
ggsave("exp2_boxplot.png", plot=p4)

# ---------- 5. tidyr ----------
# install.packages("tidyr")
library(tidyr)
cat("\\n--- tidyr ---\\n")

# Pivot longer
df_long <- pivot_longer(df, cols=c(Salary, Bonus),
                        names_to="Type", values_to="Amount")
cat("Pivot Longer:\\n")
print(df_long)

# Pivot wider
df_wide <- pivot_wider(df_long, names_from=Type, values_from=Amount)
cat("\\nPivot Wider:\\n")
print(df_wide)

# ---------- 6. readr ----------
# install.packages("readr")
library(readr)
cat("\\n--- readr ---\\n")

# Write CSV
write_csv(df, "exp2_sample_data.csv")
cat("CSV written: exp2_sample_data.csv\\n")

# Read CSV back
df_read <- read_csv("exp2_sample_data.csv")
cat("CSV read back:\\n")
print(df_read)

# ---------- 7. stringr ----------
# install.packages("stringr")
library(stringr)
cat("\\n--- stringr ---\\n")

names_vec <- c("Alice Smith", "Bob Jones", "Charlie Brown")
cat("Original:", names_vec, "\\n")
cat("Uppercase:", str_to_upper(names_vec), "\\n")
cat("Contains 'Bob':", str_detect(names_vec, "Bob"), "\\n")
cat("Replace 'Smith' with 'Doe':", str_replace(names_vec, "Smith", "Doe"), "\\n")
cat("String length:", str_length(names_vec), "\\n")

# ---------- 8. lubridate ----------
# install.packages("lubridate")
library(lubridate)
cat("\\n--- lubridate ---\\n")

today_date <- today()
cat("Today:", format(today_date), "\\n")
cat("Year:", year(today_date), "\\n")
cat("Month:", month(today_date), "\\n")
cat("Day:", day(today_date), "\\n")

date1 <- ymd("2024-01-01")
date2 <- ymd("2024-12-31")
cat("Days between:", as.numeric(date2 - date1), "\\n")

# ---------- 9. caret (Machine Learning) ----------
# install.packages("caret")
library(caret)
cat("\\n--- caret (Linear Regression) ---\\n")

set.seed(42)
ml_data <- data.frame(
  x1 = c(1,2,3,4,5,6,7,8,9,10),
  x2 = c(2,4,5,4,5,7,8,9,10,11),
  y  = c(3,5,7,6,8,10,11,13,14,16)
)

train_index <- createDataPartition(ml_data$y, p=0.8, list=FALSE)
train_data  <- ml_data[train_index, ]
test_data   <- ml_data[-train_index, ]

model <- train(y ~ x1 + x2, data=train_data, method="lm")
cat("Model Summary:\\n")
print(summary(model))

predictions <- predict(model, newdata=test_data)
cat("Predictions:", predictions, "\\n")
cat("Actual:     ", test_data$y, "\\n")

# ---------- 10. corrplot ----------
# install.packages("corrplot")
library(corrplot)
cat("\\n--- corrplot ---\\n")

num_df <- df[, c("Age", "Salary", "Bonus")]
corr_matrix <- cor(num_df)
cat("Correlation Matrix:\\n")
print(round(corr_matrix, 2))

png("exp2_corrplot.png")
corrplot(corr_matrix, method="color", addCoef.col="black",
         title="Correlation Matrix", mar=c(0,0,1,0))
dev.off()
cat("Correlation plot saved: exp2_corrplot.png\\n")

cat("\\n========================================")
cat("\\nExperiment 2 Complete!")
cat("\\n========================================\\n")
"""

# ============================================================
# Print the R code for reference
# ============================================================
print("=" * 60)
print("EXPERIMENT 2: Data Analytics Libraries in R")
print("=" * 60)
print("\nThis experiment uses R. Below is the complete R code.")
print("Copy and run it in RStudio or R console.\n")
print("-" * 60)
print(r_code)
print("-" * 60)

# ============================================================
# Save the R code to a .R file automatically
# ============================================================
with open("exp2_r_libraries.R", "w") as f:
    f.write(r_code.strip())

print("\nR code has also been saved to: exp2_r_libraries.R")
print("Open that file in RStudio and run it.\n")

# ============================================================
# Libraries Summary Table
# ============================================================
print("=" * 60)
print("SUMMARY: Key R Libraries for Data Analytics")
print("=" * 60)
libraries = [
    ("Base R",      "Built-in: vectors, data frames, summary, plot"),
    ("dplyr",       "Data manipulation: filter, select, mutate, group_by"),
    ("ggplot2",     "Visualizations: bar, scatter, histogram, boxplot"),
    ("tidyr",       "Data reshaping: pivot_longer, pivot_wider"),
    ("readr",       "Fast CSV/file reading and writing"),
    ("stringr",     "String operations: detect, replace, split"),
    ("lubridate",   "Date/time handling"),
    ("caret",       "Machine learning: train/test, models"),
    ("corrplot",    "Correlation matrix visualization"),
]
for lib, desc in libraries:
    print(f"  {lib:<12} → {desc}")

print("\nInstall all with:")
print('  install.packages(c("dplyr","ggplot2","tidyr","readr",')
print('                     "stringr","lubridate","caret","corrplot"))')
print("\nExperiment 2 Python wrapper complete!")
