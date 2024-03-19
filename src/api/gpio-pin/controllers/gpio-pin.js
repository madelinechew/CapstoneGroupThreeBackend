'use strict';

/**
 * gpio-pin controller
 */

const { createCoreController } = require('@strapi/strapi').factories;

module.exports = createCoreController('api::gpio-pin.gpio-pin');
