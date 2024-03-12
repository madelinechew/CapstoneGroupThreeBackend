'use strict';

/**
 * gpio controller
 */

const { createCoreController } = require('@strapi/strapi').factories;

module.exports = createCoreController('api::gpio.gpio');
