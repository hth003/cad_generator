// LEGO Brick with 2 Cylindrical Studs

// Dimensions
base_length = 31.8;
base_width = 15.8;
base_height = 9.6;
stud_diameter = 4.8;
stud_height = 2.5;
stud_wall_thickness = 1.2;
spacing_between_studs = 10.0;

// Base
module lego_brick() {
    difference() {
        // Main body
        cube([base_length, base_width, base_height]);
        
        // Internal hollowing for wall thickness (top view)
        translate([stud_diameter/2 + stud_wall_thickness, base_width/2, base_height])
            cylinder(h = base_height + stud_height, d = stud_diameter);
        translate([base_length - (stud_diameter/2 + stud_wall_thickness), base_width/2, base_height])
            cylinder(h = base_height + stud_height, d = stud_diameter);
    }
    
    // Adding studs
    translate([base_length / 2 - spacing_between_studs / 2, base_width / 2, base_height])
        cylinder(h = stud_height, d = stud_diameter);
    translate([base_length / 2 + spacing_between_studs / 2, base_width / 2, base_height])
        cylinder(h = stud_height, d = stud_diameter);
}

// Render the LEGO Brick
lego_brick();