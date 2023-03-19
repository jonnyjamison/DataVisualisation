from random import choice
#returns a randomly selected element from the specified sequence.

class RandomWalk:
    """A class to generate random walks."""
    
    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points
        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]
        
        
    def fill_walk(self):
        """Calculate all the points in the walk."""
        """Main point of this is to simulate four random decisions - will walk go right or left,
        how far in that direction, up or down, and how far in that direction"""
        
        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points: 
            
            # Decide which direction to go and how far to go in that direction.
            x_direction = choice([1, -1]) #1 is for right movement, -1 for left 

            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            
            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue
            
            # Calculate the new position.
            x = self.x_values[-1] + x_step #add the new step to previous step to make it a continuous walk
            y = self.y_values[-1] + y_step
            
            #add to list of existing values 
            self.x_values.append(x) 
            self.y_values.append(y)
            #will be added to instance's x & y_values attribute 