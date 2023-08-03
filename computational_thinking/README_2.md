# Computational Thinking Activity #2: Curve Stitching

## Activity
[Curve Stitching Activity Sheet](./student/curve_stitching/Curve-Stitching.pdf)

## General Plan
1. Talk about similarities/differences between drawing the house in MS Paint and Python
2. Start with a discussion centered around the RGB graphic
- What’s actually happening?
- How would you code this?
- Provide curves.py, which has a very basic start for the RGB function
    - Brief introduction functions as a way to compartmentalize/decompose code
- Wouldn't it be great if there were a better alternative to copy+paste+modify?
3. Introduce the basic Python for loop:  for i in range(start, stop, step):
- Code-a-long some basic demos
- Mention: [start, stop)
- Talk a bit about variables: y is a better choice for the RGB graphic
4. Walk through: 
- Drawing red lines with a for loop
- Drawing green lines with a second for loop
- Drawing blue lines with a third for loop
- Drawing all three colors with a single for loop
- Factoring out both approaches as stand-alone functions: RGB_3_loops(), RGB_1_loop()
- Code for above is in curves_solution.py
5. Students code the Grid and Curve Stitching graphics
6. Talk about the repetition of shapes from the Curve Stitching graphic to the Flower graphic
- Walk students through creating functions with parameters to reuse code
7. Infinity Curve should be considered a challenge for stronger students

## Teacher Notes