import random
import matplotlib.pyplot as plt

# Define emotions and initialize their levels
emotions = {
    "happiness": 0,
    "fear": 0,
    "anger": 0,
    "curiosity": 0,
    "boredom": 0
}

# Define actions and emotional responses
actions = {
    "explore": {"reward": 3, "curiosity": +2, "fear": +1},
    "eat": {"reward": 5, "happiness": +3, "boredom": -1},
    "rest": {"reward": 2, "happiness": +1, "boredom": +2},
    "poke": {"reward": -4, "anger": +3, "fear": +2}
}

emotion_history = {k: [] for k in emotions}

# Cap emotions within a range
def cap_emotion(value, min_val=-10, max_val=10):
    return max(min(value, max_val), min_val)

# Simulate for 50 time steps
for step in range(50):
    # Weighted decision: choose action based on current emotions
    weights = {action: sum(emotions.get(emo, 0) * change for emo, change in effects.items() if emo != "reward")
               for action, effects in actions.items()}
    if sum(weights.values()) > 0:
        action = random.choices(list(weights.keys()), weights=list(weights.values()), k=1)[0]
    else:
        action = random.choice(list(actions.keys()))  # Fallback to a random action

    print(f"\nStep {step+1}: Agent chose to {action.upper()}")

    # Apply rewards and update emotions
    for emo, change in actions[action].items():
        if emo == "reward":
            continue
        emotions[emo] = cap_emotion(emotions[emo] + change)

    # Slight decay over time to prevent infinite growth
    for emo in emotions:
        emotions[emo] = cap_emotion(emotions[emo] * 0.98)
        emotion_history[emo].append(emotions[emo])

    print(f"Emotions: {emotions}")

# Plot the emotion levels over time
plt.figure(figsize=(10, 6))
for emo, values in emotion_history.items():
    plt.plot(values, label=emo)

plt.title("Emotion Changes Over Time")
plt.xlabel("Time Step")
plt.ylabel("Emotion Level")
plt.legend()
plt.grid(True)
plt.show()
