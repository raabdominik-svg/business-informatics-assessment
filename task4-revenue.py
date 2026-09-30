# Daily revenue in HUF for Monday through Sunday
weekly_revenue = [210000, 265000, 240000, 310000, 250000, 190000, 280000]
daily_target = 250000
target_hit_count = 0

for x in weekly_revenue:
    if x >= daily_target:
      target_hit_count += 1
print ("We hit the target on {target_hit_count} days this week!")
