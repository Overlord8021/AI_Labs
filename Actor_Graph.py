from Actor import Actor

class Actor_Graph:
    def __init__(self, show_data):
        # Initialize an empty dictionary to store actors
        self.actors = {}
        
        # Iterate through each show in the provided show data
        for show in show_data:
            # Iterate through each actor in the show's cast
            for actor in show['cast']:
                # Get the actor's ID
                actor_id = actor['person']['id']
                # If the actor is not already in the graph
                if actor_id not in self.actors:
                    # Create a new Actor object and add it to the graph
                    self.actors[actor_id] = Actor(actor_id, actor['person']['name'], actor['person']['birthday'])
                    # Add the show to the actor's list of shows
                    self.actors[actor_id].add_show(show['id'], show['premiered'])
                else:
                    # If the actor is already in the graph, just add the show to their list
                    self.actors[actor_id].add_show(show['id'], show['premiered'])
                
    def __iter__(self):
        # Make the Actor_Graph iterable, yielding each actor in the graph
        for actor in self.actors.values():
            yield actor
            
    def build_relations(self):
        for actor in self:
            actor.compute_relations(self)
