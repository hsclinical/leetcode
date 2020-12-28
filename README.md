# leetcode

```
# *** Description ***:
# Use chrome inspect to check Network of page https://leetcode.com/problemset/algorithms/.
# Therefore, we found two APIs that may provide useful information

# *** API #1 ***:
# https://leetcode.com/api/problems/algorithms/
# Information:
#   question_id, question_title, question_title_slug, difficulty, frequency, progress
# Format:
#   json
curl -o algorithm.json "https://leetcode.com/api/problems/algorithms/"

# *** API #2 ***:
# https://leetcode.com/problems/api/tags/
# Information:
#   By company: name/slug/list_of_id
#   By topic:   name/slug/list_of_id
# Format:
#   json
curl -o tag.json "https://leetcode.com/problems/api/tags/"

# *** Last Update ***:
# 2020/12/28
```

**Table Structure**

```
id int,                 # map to question_id
name varchar(255),      # map to question_title
slug varchar(255),      # map to question_title_slug
topic varchar(255),
difficulty varchar(15),
company varchar(255),
frequency float,
progress float

--- Ideally, it should be normalized to multiple tables, such as question to topic, question to company.
--- They are 1 to n relationship. One question may have multiple solutions and each of them belongs to
--- different topic. Meanwhile, multiple companies may ask the same question during interview. It's better
--- to create multiple tables and use foreign key/primary key to link them.

--- However, in reality, we put everything into one table to make it easy to read
```

**Two Dimensions: Category and Difficulity**

Category [1]:
  1. Array
  2. Binary
  3. Dynamic Programming
  4. Graph
  5. Interval
  6. Linked List
  7. Matrix
  8. String
  9. Tree
  10. Heap

Difficulity:
  1. Hard
  2. Medium
  3. Easy


**Progress**

Note: Sorted based on question index


**Reference**
  1. https://leetcode.com/discuss/general-discussion/419062/list-of-leetcode-question-to-cover-all-the-concepts-and-type-of-questions
