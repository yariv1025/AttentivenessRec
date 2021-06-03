class AttentionCalc(object):
    """
    The class calculate the attention level base on the emotic model result
    """

    def __init__(self, cont_weights, ratio, alpha):
        """
        Creating AttentionCalc object for calculate the attention level.
        :param cont_weights: the weights of every continuous value
        :param ratio: the ratio between the continuous values and the emotion values
        :param alpha: the ratio between the current result and the previous result
        """
        self.p_result = 0
        self.cont_weights = cont_weights
        self.ratio = ratio
        self.alpha = alpha

        self.pos = ['Anticipation', 'Confidence', 'Engagement', 'Esteem', 'Excitement',
                    'Happiness', 'Peace', 'Surprise']

        self.neg = ['Anger', 'Annoyance', 'Aversion', 'Disapproval', 'Disconnection', 'Disquietment',
                    'Doubt/Confusion', 'Embarrassment', 'Fear', 'Sadness',
                    'Sensitivity']

        self.neutral = ['Affection', 'Pleasure', 'Sympathy', 'Fatigue', 'Pain', 'Suffering', 'Yearning']

    def emotion_value(self, emotion):
        """
        The function receives an emotion and returns it's value.

        :param emotion: an emotion
        :return: 1 if positive emotion, else -1.
        """
        if emotion in self.pos:
            return 1
        elif emotion in self.neg:
            return -1
        elif emotion in self.neutral:
            return 0
        else:
            raise ValueError("Emotion not found!")

    def emotion_calc(self, emotions):
        """
        Function for calculate the attentive levels of the subject based on emotion recognition.
        The function return value in range 0 to 10. the higher the number, the higher the level of attention.

        :param emotions: list of emotions
        :return: the subject's level of attention in scale of 0 to 10
        """
        bar = 5
        for emotion in emotions:
            bar += self.emotion_value(emotion)

        return max(0, min(10, bar))

    def cont_calc(self, cont):
        """
        Calculation of continuous values.
        :param cont: continuous weights
        :return: continuous calculation result
        """
        valence = cont[0] * self.cont_weights[0]
        arousal = cont[1] * self.cont_weights[1]
        dominance = cont[2] * self.cont_weights[2]

        return round(valence + arousal + dominance, 2)

    def attention_calc(self, results):
        """
        Calculation of attention value.
        :param results: The final result of attention level
        :return: attention level
        """
        emotion_result = self.emotion_calc(results[0])
        cont_result = self.cont_calc(results[1])

        result = emotion_result * self.ratio + cont_result * (1 - self.ratio)
        self.p_result = result * self.alpha + self.p_result * (1 - self.alpha)
        print(self.p_result)
        return self.p_result
