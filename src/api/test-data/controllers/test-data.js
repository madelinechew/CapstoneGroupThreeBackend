'use strict';

/**
 * test-data controller
 */

const { createCoreController } = require('@strapi/strapi').factories;

module.exports = createCoreController('api::test-data.test-data');
