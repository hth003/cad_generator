module gear_module(N=12, m=2, pressure_angle=20, addendum=2, dedendum=2.5, clearance=0.5, hub_diameter=10, hub_length=5){
    pitch_diameter = m * N;
    outside_diameter = pitch_diameter + 2 * addendum;
    root_diameter = pitch_diameter - 2 * dedendum;

    // Approximated gear -  more accurate gear generation requires a more complex algorithm.
    difference(){
        cylinder(h=m, d=outside_diameter);
        translate([0,0,-m/2])cylinder(h=m*2, d=root_diameter);
    }

    // Hub
    translate([0,0,-hub_length/2])cylinder(h=hub_length, d=hub_diameter);
}

gear_module();