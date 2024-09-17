class Actor:
    def __init__(self, actor_id, actor_name, actor_birthday):
        # Initialize actor attributes
        self._id = actor_id
        self.name = actor_name
        self.birthday = actor_birthday
        self.actor_characterNames = {}  # Dictionary to store character names for each show
        self.actor_shows = {}  # Dictionary to store premiere dates for each show
        self.related_actors = {}  # Dictionary to store related actors and the weight of the relation
    
    @property
    def id(self):
        return self._id
    
    def __contains__(self, show_id):
        # Returns True if the actor is in the show, False otherwise
        return show_id in self.actor_shows
        
    def add_show(self, show_id, premiere_date):
        # Add a show to the actor's list of shows if it's not already present
        if show_id not in self.actor_shows:
            self.actor_shows[show_id] = premiere_date
            
    def add_character(self, show_id, character_name):
        # Add a character name for a specific show if it's not already present
        if show_id not in self.actor_characterNames:
            self.actor_characterNames[show_id] = character_name

    def __str__(self):
        # Create a string representation of the actor
        # List all show IDs the actor has participated in
        show_list = ", ".join(str(show_id) for show_id in self.actor_shows.keys())
        return f"{self.name}, shows: {show_list}, influence: {self.compute_influence()}"
    
    def add_relation(self, actor_id):
        if actor_id != self.id:
            if actor_id not in self.related_actors:
                self.related_actors[actor_id] = 1
            else:
                self.related_actors[actor_id] += 1
        
    def compute_relations(self, graph):
        for actor in graph:
            for show in actor.actor_shows:
                if show in self.actor_shows:
                    self.add_relation(actor.id)
                    
    # def print_relations(self):
    #     for actor_id, weight in self.related_actors.items():
    #         print(f"{self.name}" + " " + str(self.compute_influence()))
            
    def compute_influence(self):
        # Check if there are any relationships
        if not self.related_actors:
            return 0
        
        # Calculate the average of relationship weights
        total_weight = sum(self.related_actors.values())
        num_relationships = len(self.related_actors)
        
        return total_weight / num_relationships
