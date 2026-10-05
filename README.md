# Programming Lab Archive

My Java and Python laboratory/exam submissions, collected from individual GitHub Classroom repositories into one archive.

These are historical learning exercises, preserved as submitted. They demonstrate sorting, data structures, search, recursion, object-oriented programming, and NumPy array operations. They are not a production library; existing limitations and mistakes are retained.

## Exercises

| Week | Language | Topic |
| --- | --- | --- |
| 01 | Java | [Odd-even sorting and duplicate removal](java/week-01/) |
| 02 | Java | [Circular linked lists](java/week-02/) |
| 03 | Java | [Linked stacks and balanced brackets](java/week-03/) |
| 05 | Java | [Dynamic array stack](java/week-05/) |
| 07 | Java | [Linear and binary search](java/week-07/) |
| 08 | Java | [Recursive algorithms and complexity](java/week-08/) |
| 09 | Python | [Expense tracker](python/week-09/) |
| 10 | Python | [Object-oriented hospital simulation](python/week-10/) |
| 11 | Python | [Air quality analysis with NumPy](python/week-11/) |
| 12 | Python | [Room temperature analysis with NumPy](python/week-12/) |

Only the available submissions are included; weeks 04 and 06 were not part of the supplied repository set.

## Running the examples

Each week is independent. Compile Java examples separately because several weeks use the same class names.

Use JDK 25 or newer: weeks 01, 02, and 03 use compact source files with an instance `main` method.

```sh
cd java/week-02
javac *.java
java Main
```

Java entry classes: `Main` for weeks 01, 02, 03, and 07; `ArrayStack` for week 05; `RecursiveAlgorithmLab` for week 08.

Python examples require Python 3. NumPy is required for weeks 11 and 12.

```sh
python -m pip install -r requirements.txt
python python/week-09/expense_tracker.py
python python/week-10/hospital_management_system.py
python python/week-11/air_quality.py
python python/week-12/room_temperatures.py
```

## Archive preparation

- Source code contents are preserved byte for byte.
- Student-number folder names have been removed; the week 12 script has a descriptive filename.
- The two identical copies of week 02 source files are included once.
- Compiled `.class` files, IDE metadata, and Classroom invitation/deadline badges are excluded.
- The original private repositories and their histories remain intact. This archive starts with a new Git history.

## Known limitations

Week 03 can raise an exception when a closing bracket is encountered with an empty stack. Week 07's endpoint comparison is not a complete sortedness check. Week 02's `print` and `rotate` methods assume a nonempty list. These behaviors are retained to keep the archive faithful to the original submissions.
