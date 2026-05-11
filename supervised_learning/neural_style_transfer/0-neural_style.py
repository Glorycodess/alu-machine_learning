#!/usr/bin/env python3
"""
Neural Style Transfer class for TensorFlow 1.12
"""

import numpy as np
import tensorflow as tf


class NST:
    """
    Performs tasks for Neural Style Transfer
    """

    style_layers = [
        'block1_conv1',
        'block2_conv1',
        'block3_conv1',
        'block4_conv1',
        'block5_conv1'
    ]
    content_layer = 'block5_conv2'

    def __init__(self, style_image, content_image, alpha=1e4, beta=1):
        """
        Class constructor for Neural Style Transfer

        Args:
            style_image (np.ndarray): shape (h, w, 3)
            content_image (np.ndarray): shape (h, w, 3)
            alpha (float): weight for content cost
            beta (float): weight for style cost
        """
        # Type checks
        if (not isinstance(style_image, np.ndarray) or
                style_image.ndim != 3 or style_image.shape[2] != 3):
            raise TypeError(
                "style_image must be a numpy.ndarray with shape (h, w, 3)"
            )
        if (not isinstance(content_image, np.ndarray) or
                content_image.ndim != 3 or content_image.shape[2] != 3):
            raise TypeError(
                "content_image must be a numpy.ndarray with shape (h, w, 3)"
            )
        if not isinstance(alpha, (int, float)) or alpha < 0:
            raise TypeError("alpha must be a non-negative number")
        if not isinstance(beta, (int, float)) or beta < 0:
            raise TypeError("beta must be a non-negative number")

        # Enable eager execution (TensorFlow 1.12)
        tf.enable_eager_execution()

        # Store preprocessed images
        self.style_image = self.scale_image(style_image)
        self.content_image = self.scale_image(content_image)
        self.alpha = alpha
        self.beta = beta

    @staticmethod
    def scale_image(image):
        """
        Rescales an image so pixel values are between 0 and 1
        and largest side is 512 pixels

        Args:
            image (np.ndarray): shape (h, w, 3)

        Returns:
            tf.Tensor: shape (1, h_new, w_new, 3)
        """
        if (not isinstance(image, np.ndarray) or image.ndim != 3 or
                image.shape[2] != 3):
            raise TypeError(
                "image must be a numpy.ndarray with shape (h, w, 3)"
            )

        h, w = image.shape[0], image.shape[1]

        # Always scale so largest side = 512 (scale up OR down)
        scale_factor = 512.0 / max(h, w)
        new_h = int(round(h * scale_factor))
        new_w = int(round(w * scale_factor))

        # Ensure at least 1 pixel in each dimension
        new_h = max(1, new_h)
        new_w = max(1, new_w)

        # Normalize to [0, 1] and add batch dimension
        image_float = image.astype(np.float32) / 255.0
        image_tensor = tf.convert_to_tensor(image_float[np.newaxis, ...])

        # Resize with bicubic interpolation
        resized = tf.image.resize_images(
            image_tensor,
            [new_h, new_w],
            method=tf.image.ResizeMethod.BICUBIC
        )

        # Clip values to [0, 1] to remove overshoot from bicubic interpolation
        resized = tf.clip_by_value(resized, 0.0, 1.0)

        return resized
