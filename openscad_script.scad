$fn=100;
module gear(N=12, m=2, face_width=10, pressure_angle=20) {
  d = m * N;
  a = m;
  b = 1.25 * m;
  p = PI * m;
  db = d * cos(pressure_angle);
  Do = d + 2 * a;
  Dr = d - 2 * b;
  t = p / 2;

  // Approximate involute profile with a polygon (simplified)
  points = [
    [0, a],
    [t/4, a - 0.2*a],
    [t/2, a - 0.5*a],
    [3*t/4, a - 0.7*a],
    [t, b],
  ];

  module tooth() {
    polygon(points);
  }

  // Create the gear
  for (i = [0:N-1]) {
    rotate([0, 0, i * 360 / N])
    translate([d/2, 0, 0])
    rotate([0,90,0])
    tooth();
  }

  // Create the gear body
  difference() {
    cylinder(h=face_width, r=Do/2, $fn=100);
    for (i = [0:N-1]) {
      rotate([0, 0, i * 360 / N])
      translate([d/2, 0, 0])
      rotate([0,90,0])
      tooth();
      
    }
  }
}

gear();