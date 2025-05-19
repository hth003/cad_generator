tray_length = 300;
tray_width = 200;
tray_height = 50;
corner_radius = 5;

difference() {
  cube([tray_length, tray_width, tray_height], center = true);
  translate([-tray_length/2 + corner_radius, -tray_width/2 + corner_radius, -tray_height/2])
  rotate([0,0,0])
  cube([tray_length - 2 * corner_radius, tray_width - 2 * corner_radius, tray_height], center = true);
}

rotate([45, 30, 0])
translate([20, 20, 20])
cylinder(h=10, r=3);