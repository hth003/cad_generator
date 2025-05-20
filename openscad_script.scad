// Variable assignments
length = 80;       // Length of the block in mm
width = 60;        // Width of the block in mm
height = 10;       // Height of the block in mm
pocket_diameter = 22; // Diameter of the circular pocket in mm
pocket_depth = height; // Depth of the pocket is equal to the height of the block
pocket_radius = pocket_diameter / 2; // Radius of the pocket

// Module to create the rectangular block
module rectangular_block() {
    cube([length, width, height]);
}

// Module to create the circular pocket
module circular_pocket() {
    translate([length / 2, width / 2, 0]) // Centering the pocket
        cylinder(h = pocket_depth, r = pocket_radius, center = true);
}

// Final object assembly
difference() {
    rectangular_block(); // Create the block
    circular_pocket();   // Create the pocket by subtracting from the block
}