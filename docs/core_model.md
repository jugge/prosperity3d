# Core Model – TrueProsperity

```mermaid
graph TD

subgraph Reality["Reality"]
    subgraph Entity["the Entity"]
        subgraph map["internal map of Reality"]
            self_image["Self Image Representats: the Entity"]
	    end
  end
end
```


Reality is not a class.
Reality is where all classes exist.

to manifest something is to take it from the internal map and change things in reality. i.e. manifest from internal map to Reality
to integrate something is let reality update the internal map



```mermaid
%% Entity is an actor within Reality
%% InternalMap is a part of Entity
%% SelfImage lives within the map

classDiagram    
	class Entity{
      -manifest()
	  -integrate()
    }
    
	class InternalMap{
    }
	
	class SelfImage {
	}
	     
	Entity *-- InternalMap
	InternalMap *-- SelfImage
```