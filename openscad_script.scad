module cylinder_part() {
    // Parameters
    D = 50;                    // Outer Diameter in mm
    H = 100;                   // Height in mm
    wall_thickness = 2;        // Wall thickness in mm, 0 for solid
    
    // Derived values
    inner_diameter = D - 2 * wall_thickness;
    
    // Check if hollow or solid
    if (wall_thickness > 0 && inner_diameter > 0) {
        difference() {
            cylinder(h = H, d = D, center = false);
            translate([0,0,0])  // Inner cylinder starts at bottom as well
                cylinder(h = H, d = inner_diameter, center = false);
        }
    } else {
        cylinder(h = H, d = D, center = false);
    }
}

cylinder_part();