import Array "mo:base/Array";
import Debug "mo:base/Debug";

actor Chat {

  stable var w1 = 1.0;
  stable var w2 = 1.0;
  stable var w3 = 1.0;
  stable var updatedWeight = 1.0;

  // Get the value of the current message and return it.
  public query func get1() : async Float {
    return w1;
  };

  public query func get2() : async Float {
    return w2;
  };

  public query func get3() : async Float {
    return w3;
  };

  //public var weights=[];

  // Set the value of the message (overwrite the previous value)
  public func set1(updatedw1 : Float) : async () {
    w1 := updatedw1;
    //push into weights array
  };

  public func set2(updatedw2 : Float) : async () {
    w2 := updatedw2;
    //push into weights array
  };

  public func set3(updatedw3 : Float) : async () {
    w3 := updatedw3;
    //push into weights array
  };

  stable var permission1 = 0;
  stable var permission2 = 0;
  stable var permission3 = 0;

  public func permit1(p1 : Nat) : async () {
    permission1 := p1;
  };

  public func permit2(p2 : Nat) : async () {
    permission2 := p2;
  };

  public func permit3(p3 : Nat) : async () {
    permission3 := p3;
  };

  public func updateWeights() {
    if (permission1 == 1 and permission2 == 1 and permission3 == 1) {
      updatedWeight := (w1 +w2 +w3) / 3;
    } else {
      Debug.print("Consensus not achieved");
    };
  };

  public query func getWeight() : async Float {
    return updatedWeight;
  };

};
